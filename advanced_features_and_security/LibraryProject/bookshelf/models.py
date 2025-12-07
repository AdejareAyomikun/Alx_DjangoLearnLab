from django.db import models
from django.db import AbstractUser
from django.db import BaseUserManager

class Book(models.Model):
    # Book Title (required, up to 200 characters)
    title = models.CharField(max_length=200)

    # Book Author (required, up to 100 characters)
    author = models.CharField(max_length=100)

    # Year the book was published
    publication_year = models.IntegerField()

    # Recommended: Define a human-readable representation for the object
    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)
    
    def can_create(self, user):
        return user.is_active and user.is_staff
    
    def can_view(self, user):
        return self.is_active and (self.is_staff or self == user)
    
    def can_edit(self, user):
        return self.is_active and self == user
    
    def can_delete(self, user):
        return self.is_active and self == user