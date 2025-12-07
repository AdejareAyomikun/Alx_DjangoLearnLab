from django.db import models
from django.db import models 

class Book(models.Model):
    title = models.CharField(max_length=255, help_text="The title of the book.")
    author = models.CharField(max_length=255, help_text="The name of the book's author.")
    
    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        ordering = ['title']
        verbose_name = "Book"
        verbose_name_plural = "Books"