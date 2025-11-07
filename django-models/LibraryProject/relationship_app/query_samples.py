from relationship_app.models import Author, Book, Library, Librarian


def create_sample_data():
    author1 = Author.objects.create(name="Jane Austen")
    author2 = Author.objects.create(name="George Orwell")

    book1 = Book.objects.create(title="Pride and Prejudice", author=author1)
    book2 = Book.objects.create(title="Emma", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)

    library_a = Library.objects.create(name="Central City Library")
    library_b = Library.objects.create(name="University Archives")

    library_a.books.add(book1, book3)
    library_b.books.add(book2, book3, book4)

    librarian_a = Librarian.objects.create(
        name="Alice Smith", library=library_a)
    librarian_b = Librarian.objects.create(
        name="Bob Johnson", library=library_b)

    print("Sample data created successfully.")


def query_books_by_author(author_name):
    """Query all books by a specific author (ForeignKey reverse relationship)."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\n📚 Books by {author_name} (using objects.filter()):")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"\nAuthor '{author_name}' not found.")

def query_books_in_library(library_name):
    """List all books in a library (ManyToManyField)."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all() 
        print(f"\n📖 Books in '{library_name}':")
        for book in books:
            print(f"- {book.title} (by {book.author.name})")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")

def query_librarian_for_library(library_name):
    """Retrieve the librarian for a library (OneToOneField reverse relationship)."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian 
        print(f"\n👤 Librarian for '{library_name}':")
        print(f"- {librarian.name}")
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian found for '{library_name}'.")