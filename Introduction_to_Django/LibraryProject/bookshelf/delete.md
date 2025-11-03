# Retrieve the updated book instance
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
# Delete the instance from the database
book_to_delete.delete()
# Confirm deletion by trying to retrieve all books
print(Book.objects.all())

# Retrieve the updated book instance
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
# Delete the instance from the database
book_to_delete.delete()
# Confirm deletion by trying to retrieve all books
print(Book.objects.all())