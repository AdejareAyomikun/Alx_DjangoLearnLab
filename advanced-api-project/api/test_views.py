from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from datetime import datetime

from api.models import Author, Book
from api.serializers import BookSerializer

class BookAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="Jane Austen")
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.auth_client = APIClient()
        logged_in = self.client.login(username='testuser', password='password123')
        self.assertTrue(logged_in)
    
        self.book1 = Book.objects.create(
            title="Pride and Prejudice", 
            publication_year=1813, 
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Sense and Sensibility", 
            publication_year=1811, 
            author=self.author
        )
        
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})

    def get_auth_client(self):
        client = APIClient()
        client.login(username='testuser', password='password123')
        return client


    def test_book_list_retrieval(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_book_create_authenticated(self):
        auth_client = self.get_auth_client()
        new_book_data = {
            'title': 'Mansfield Park',
            'publication_year': 1814,
            'author': self.author.pk 
        }
        response = auth_client.post(self.create_url, new_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'Mansfield Park')

    def test_book_detail_retrieval(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_book_update_authenticated(self):
        auth_client = self.get_auth_client()
        updated_data = {
            'title': 'Pride and Prejudice (Revised)',
            'publication_year': 1813,
            'author': self.author.pk
        }
        response = auth_client.put(self.update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Pride and Prejudice (Revised)')

    def test_book_delete_authenticated(self):
        auth_client = self.get_auth_client()
        response = auth_client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_book_create_unauthenticated_fails(self):
        new_book_data = {
            'title': 'Persuasion',
            'publication_year': 1817,
            'author': self.author.pk
        }
        response = self.client.post(self.create_url, new_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 2)

    def test_book_update_unauthenticated_fails(self):
        original_title = self.book1.title
        updated_data = {
            'title': 'Attempted Update',
            'publication_year': 1813,
            'author': self.author.pk
        }
        response = self.client.put(self.update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, original_title)

    def test_book_delete_unauthenticated_fails(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Book.objects.filter(pk=self.book1.pk).exists())

    def test_book_create_future_year_fails(self):
        auth_client = self.get_auth_client()
        future_year = datetime.now().year + 1
        invalid_data = {
            'title': 'The Book of Tomorrow',
            'publication_year': future_year,
            'author': self.author.pk
        }
        response = auth_client.post(self.create_url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
        self.assertIn('Publication year cannot be in the future.', response.data['publication_year'])
        self.assertEqual(Book.objects.count(), 2)

    def test_book_list_search_by_title(self):
        response = self.client.get(self.list_url, {'search': 'Prejudice'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    def test_book_list_filter_by_year_range(self):
        response = self.client.get(self.list_url, {'publication_year__gte': 1813})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    def test_book_list_ordering_descending(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], self.book1.title)
        self.assertEqual(response.data[1]['title'], self.book2.title)