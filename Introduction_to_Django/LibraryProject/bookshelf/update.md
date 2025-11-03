# Retrieve the book instance
book_to_update = Book.objects.get(title="1984")
# Update the title attribute
book_to_update.title = "Nineteen Eighty-Four"
# Save the changes to the database
book_to_update.save()
print(book_to_update.title)

# Expected Output:
# Nineteen Eighty-Four
# (The output confirms the field has been updated.)