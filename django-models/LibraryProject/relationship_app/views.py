from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

def book_list_fbv(request):
    """Lists all books using a function-based view."""
    # Retrieve all Book objects
    all_books = Book.objects.all().select_related('author')
    
    context = {
        'books': all_books,
        'view_type': 'Function-Based View'
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """Displays details for a specific library using a DetailView CBV."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' 

    def get_context_data(self, **kwargs):
        """Adds custom context data to the template."""
        context = super().get_context_data(**kwargs)
        context['view_type'] = 'Class-Based View'
        return context