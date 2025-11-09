from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import LogoutView
from .views import LoginView
from .views import LibraryDetailView
from .views import list_books
from .views import register

urlpatterns = [
    path('', views.list_books, name='book_list_root'),
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('admin_area/', views.admin_view, name='admin_area'),
    path('librarian_area/', views.librarian_view, name='librarian_area'),
    path('member_area/', views.member_view, name='member_area'),
    path('books/add/', views.add_book, name='book_add/'),
    path('books/edit/<int:pk>/', views.edit_book, name='book_edit/'),
    path('books/delete/<int:pk>/', views.delete_book, name='book_delete'),
]