from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [] 
        
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated]

        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        
        else:
            permission_classes = [IsAuthenticated] 

        return [permission() for permission in permission_classes]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer