from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email is mandatory")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
