from django.contrib import admin
from django.db.models import Count
from django import forms

from .models import Author
from django.utils.translation import gettext_lazy as _


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['books'].required = False


class BookCountFilter(admin.SimpleListFilter):
    title = _('Book count')
    parameter_name = 'book_count'

    def lookups(self, request, model_admin):
        return (
            ('0', _('0 Books')),
            ('1', _('1 Book')),
            ('2+', _('2+ Books')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.annotate(num_books=Count('books')).filter(num_books=0)
        if self.value() == '1':
            return queryset.annotate(num_books=Count('books')).filter(num_books=1)
        if self.value() == '2+':
            return queryset.annotate(num_books=Count('books')).filter(num_books__gt=1)


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    form = AuthorForm
    list_display = ('id', 'name', 'surname', 'patronymic', 'get_books', 'sum_books_author_have')
    list_filter = ('surname', BookCountFilter)
    list_display_links = ('name', 'surname',)
    search_fields = ('name', 'surname',)
    readonly_fields = ('get_books', 'sum_books_author_have')
    ordering = ['id', 'surname']
    fieldsets = (
        ('Name', {
            'fields': ('name', 'surname', 'patronymic')
        }),
        ('Modifiable Information', {
            'fields': ('books',)
        }),
    )

    def get_books(self, obj):
        return '  \n  '.join([str(i) + ')' + book.name for i, book in enumerate(obj.books.all(), 1)])
    get_books.short_description = 'Books'

    def sum_books_author_have(self, obj):
        return len(obj.books.all())
    sum_books_author_have.short_description = 'amount_books'

