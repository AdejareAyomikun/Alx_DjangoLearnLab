from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

def list_books(request):
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
    
class UserLoginView(login):
    template_name = 'registration/login.html'

class UserLogoutView(logout):
    template_name = 'registration/logged_out.html'
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'form': form}
            return render(request, 'registration/register.html', context)
        