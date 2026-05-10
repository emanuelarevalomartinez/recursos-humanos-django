import uuid 
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField( max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('user', 'User'),
    ], default='user')

    def __str__(self):
        return f"{self.email}"
