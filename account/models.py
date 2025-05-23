from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True,null = True)

    def __str__(self):
        return self.get_full_name() or self.username  # ✅ Correct usage
