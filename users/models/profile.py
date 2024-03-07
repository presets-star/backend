from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

from presets.models.presets import Preset


User = get_user_model()


class Profile(models.Model):

    date_birth = models.DateField(blank=True, null=True)

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    favourites = models.ManyToManyField(Preset, blank=True)

    buys = models.IntegerField(blank=True, null=True)
    sold = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    subscribers = models.PositiveIntegerField(default=0)
    tracks = models.PositiveIntegerField(default=0)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    email = models.EmailField()

    gender = models.CharField(
        max_length=1, choices=(("M", "male"), ("F", "female")), blank=True, null=True
    )

    phone = PhoneNumberField(max_length=20)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
