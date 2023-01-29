
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.URLField(default="https://via.placeholder.com/150", max_length=200)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(unique=True)

    # bio= models.TextField()
    

    def __str__(self):  # The __str__ method just tells Django what to print when it needs to print out an instance of the User model.
        return self.username
