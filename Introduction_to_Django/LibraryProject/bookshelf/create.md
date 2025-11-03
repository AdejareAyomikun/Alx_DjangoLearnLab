from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book.title)


# Expected Output:
# 1984
# (The output confirms the object was created and the title is accessible.)
