# relationship_app/admin.py
from django.contrib import admin
from .models import Author, Book, Library, Librarian # Import all models

# 1. Author Model Registration (One-to-Many side)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Display 'name' in the list view
    list_display = ('name',)
    # Allow searching by name
    search_fields = ('name',)

# ---

# 2. Book Model Registration (ForeignKey relationship)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display 'title' and the related 'author' in the list view
    list_display = ('title', 'author',)
    # Allow filtering by author
    list_filter = ('author',)
    # Allow searching by title
    search_fields = ('title',)

# ---

# 3. Library Model Registration (ManyToMany relationship)
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # Use filter_horizontal to manage the ManyToMany 'books' field,
    # which provides a cleaner interface for selecting multiple books.
    filter_horizontal = ('books',) 

# ---

# 4. Librarian Model Registration (One-to-One relationship)
@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    # Display 'name' and the related 'library' in the list view
    list_display = ('name', 'library',)
    # Allow searching by name
    search_fields = ('name',)