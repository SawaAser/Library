from django.contrib import admin
from .models import Order
from django.contrib.admin import SimpleListFilter


class BookFilter(SimpleListFilter):
    title = 'book'
    parameter_name = 'book'

    def lookups(self, request, model_admin):
        books = set([(o.book.id, o.book.name) for o in model_admin.model.objects.all()])
        return sorted(books, key=lambda x: x[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(book__id__exact=self.value())
        return queryset


class UserFilter(SimpleListFilter):
    title = 'user'
    parameter_name = 'user'

    def lookups(self, request, model_admin):
        users = set([(o.user.id, f"{o.user.first_name} {o.user.middle_name} {o.user.last_name}")
                    for o in model_admin.model.objects.all()])
        return sorted(users, key=lambda x: x[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user__id__exact=self.value())
        return queryset


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'get_user_name', 'get_book_title', 'created_at', 'end_at', 'plated_end_at')
    list_filter = (BookFilter, UserFilter)
    search_fields = ('book__name', 'user__first_name', 'user__last_name')
    readonly_fields = ('created_at', 'end_at',)
    ordering = ['created_at', 'plated_end_at',]
    fieldsets = (
        ('Fixed Information', {
            'fields': ('created_at', 'end_at',)
        }),
        ('Modifiable Information', {
            'fields': ('user', 'book')
        }),
        ('Important Dates', {
            'fields': ('plated_end_at',),
        }),
    )

    def get_user_name(self, obj):
        return obj.user.first_name + ' ' + obj.user.middle_name + ' ' + obj.user.last_name

    get_user_name.short_description = 'User Name'

    def get_book_title(self, obj):
        return obj.book.name

    get_book_title.short_description = 'Book Title'
