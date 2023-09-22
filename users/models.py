from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.



class CustomUser(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __str__(self) -> str:
        return self.email
    

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Profile of {self.user.username}'

class LoginHistory(models.Model):
    user = models.CharField(max_length=60, null=True)
    login_time = models.DateTimeField(auto_now=True)
    login_result = models.BooleanField()
