from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class YourModel(models.Model):
    created_at = models.DateTimeField(default=datetime.now)


class User(AbstractUser):
    class Role(models.TextChoices):
        USERS = 'USERS', 'User'
        DEALER = 'DEALER', 'Dealer'

    is_dealer = models.BooleanField(default=False)
    role = models.CharField(max_length=6, choices=Role.choices, default=Role.USERS)

class Product(models.Model):
    Productname = models.CharField(max_length=100)
    title = models.TextField()
    Productprice = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.URLField(max_length=100)
    dealer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True) 

    def __str__(self):
        return f"Wishlist for {self.user.username}"