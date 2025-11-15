from django.contrib import admin
from .models import Book


class BookShelf(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')
    list_display_links = ('title',)


admin.site.register(Book, BookShelf)