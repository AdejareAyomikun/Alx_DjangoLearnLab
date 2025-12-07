import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    publication_year_gt = django_filters.NumberFilter(
        field_name='publication_year', 
        lookup_expr='gt'
    )
    
    author_name = django_filters.CharFilter(
        field_name='author__name', 
        lookup_expr='icontains'
    )

    class Meta:
        model = Book
        fields = {
            'publication_year': ['exact', 'gte', 'lte'],
            'title': ['icontains'],
        }