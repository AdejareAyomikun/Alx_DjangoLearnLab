# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    A ModelForm for creating and editing Book instances.
    It automatically generates form fields based on the Book model.
    """
    class Meta:
        model = Book
        # Fields to include in the form
        fields = ['title', 'author', 'publication_date', 'isbn'] 
        
        # Optional: Add human-readable labels
        labels = {
            'title': 'Book Title',
            'author': 'Author',
            'publication_date': 'Publication Date',
            'isbn': 'ISBN Number',
        }