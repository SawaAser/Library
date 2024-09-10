from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.html import format_html
from django.urls import reverse
from author.models import Author
from .models import Book, Genre


class AuthorFilter(SimpleListFilter):
    title = 'author'
    parameter_name = 'author'

    def lookups(self, request, model_admin):
        authors = set(
            (author.id, f"{author.surname} {author.patronymic} {author.name}")
            for book in Book.objects.prefetch_related('authors').all()
            for author in book.authors.all()
        )
        return sorted(authors, key=lambda x: x[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(authors__id=self.value())
        return queryset


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'image_tag', 'name', 'get_authors', 'publication_year', 'get_genres', 'count', 'get_description'
    )
    list_display_links = ('image_tag', 'name')
    list_filter = (AuthorFilter, 'name', 'id', 'publication_year')
    search_fields = (
        'name', 'authors__surname', 'authors__patronymic', 'authors__name', 'publication_year'
    )
    ordering = ['name', 'id', 'count', 'publication_year']

    fieldsets = (
        ('Read-Only Information', {
            'fields': ('name', 'get_authors_list', 'publication_year'),
        }),
        ('Editable Information', {
            'fields': ('description', 'genres', 'image'),
        }),
        ('Important Dates', {
            'fields': ('date_of_issue',),
        }),
    )

    readonly_fields = ('image_tag', 'get_authors', 'get_description', 'get_authors_list')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" height="100" />', obj.image.url)
        return 'No image'

    image_tag.short_description = 'Image'

    def get_authors(self, obj):
        return '  \n  '.join([
            f"{i}) {author.surname} {author.patronymic} {author.name}"
            for i, author in enumerate(obj.authors.all(), 1)
        ])

    get_authors.short_description = 'Authors'

    def get_genres(self, obj):
        return '  \n  '.join([
            f"{i}) {genre.name}"
            for i, genre in enumerate(obj.genres.all(), 1)
        ])

    get_genres.short_description = 'Genres'

    def get_description(self, obj):
        return obj.description[:300] + '...'

    get_description.short_description = 'Short Description'

    def get_authors_list(self, obj):
        author_ids = obj.authors.values_list('id', flat=True)
        authors = Author.objects.filter(id__in=author_ids)

        links = [
            format_html(
                '<a href="{}">{}</a>',
                reverse('admin:author_author_change', args=[author.pk]),
                f'{author.name} {author.surname}'
            )
            for author in authors
        ]
        return format_html('<br>'.join(links))


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('name',)
