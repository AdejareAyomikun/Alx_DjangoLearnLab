from django.contrib import admin
from .models import Book
from .models import CustomUser


class BookShelf(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')
    list_display_links = ('title',)
    
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth')
    search_fields = ('username', 'email')


admin.site.register(Book, BookShelf)
admin.site.register(CustomUser, CustomUserAdmin)