# Retrieve the book instance
book = Book.objects.get(title="1984")
# Update the title attribute
book.title = "Nineteen Eighty-Four"
# Save the changes to the database
book.save()
print(book.title)

# Expected Output:
# Nineteen Eighty-Four
# (The output confirms the field has been updated.)