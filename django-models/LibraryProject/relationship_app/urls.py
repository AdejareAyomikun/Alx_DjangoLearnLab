from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
    path('', views.list_books, name='book_list_root'),
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/relationship_app/login/'), name='logout'),
    path('register/', views.register, name='register',)
]