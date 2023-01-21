
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):  # The __str__ method just tells Django what to print when it needs to print out an instance of the User model.
        return self.username