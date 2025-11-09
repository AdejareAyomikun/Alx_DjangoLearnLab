from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .utils import is_admin, is_librarian, is_member
from django.conf import settings
from .models import Book
from .models import Library


@permission_required('relationship_app.can_add_book', login_url='/relationship_app/login/')
def add_book(request):
    """Placeholder view for adding a new book."""
    return render(request, 'relationship_app/book_form.html', {'action': 'Add Book'})

@permission_required('relationship_app.can_change_book', login_url='/relationship_app/login/')
def edit_book(request, pk):
    """Placeholder view for editing an existing book."""
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/book_form.html', {'action': f'Edit Book: {book.title}'})

# Permission required: relationship_app.can_delete_book
@permission_required('relationship_app.can_delete_book', login_url='/relationship_app/login/')
def delete_book(request, pk):
    """Placeholder view for deleting a book."""
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"Book '{book.title}' successfully deleted (Placeholder).", status=200)

def list_books(request):
    """Lists all books using a function-based view."""
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


class LoginView(LoginView):
    template_name = 'registration/login.html'


class LogoutView(LogoutView):
    template_name = 'registration/logged_out.html'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
            context = {'form': form}
            return render(request, 'relationship_app/register.html', context)

@user_passes_test(is_admin, login_url=settings.LOGIN_URL)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})

@user_passes_test(is_librarian, login_url=settings.LOGIN_URL)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})

@user_passes_test(is_member, login_url=settings.LOGIN_URL)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})