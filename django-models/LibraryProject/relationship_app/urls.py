from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    path('books/', views.book_list_fbv, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]