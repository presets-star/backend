from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()
genders = ("male", "female", "helicopter")


class Profile(models.Model):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    date_birth = models.DateField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    favourites = models.ManyToManyField("Preset", blank=True)
    buys = models.IntegerField(blank=True, null=True)
    sold = models.IntegerField(blank=True, null=True)
    subscribers = models.PositiveIntegerField(default=0)
    tracks = models.PositiveIntegerField(default=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField(max_length=20)
    gender = models.Choices(genders)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
