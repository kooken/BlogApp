from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import validate_email_domain


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name='email',
        validators=[validate_email_domain]
    )
    phone = models.CharField(max_length=35, verbose_name='phone number', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='date of birth', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='date of user creation')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='date of user update')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
