from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class User(AbstractUser):

    phone_number = PhoneNumberField(
        "Phone number", unique=True, null=True, max_length=20
    )

    # USERNAME_FIELD = ''
    # REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
