from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name="Image")

    class Meta:
        db_table = "User"
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        return self.username