from django.db import models


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