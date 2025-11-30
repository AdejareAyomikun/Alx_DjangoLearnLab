from django.db import models
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="The unique name of the product.")
    description = models.TextField(help_text="A detailed description of the product.")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="The price of the product (e.g., 99.99).")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Product"
        verbose_name_plural = "Products"