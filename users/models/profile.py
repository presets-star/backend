from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):

    date_birth = models.DateField(blank=True, null=True)

    user_id = models.OneToOneField('users.User', on_delete=models.CASCADE)
    favourites = models.ManyToManyField('presets.Preset', blank=True)

    buys = models.IntegerField(blank=True, null=True)
    sold = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    subscribers = models.PositiveIntegerField(default=0)
    tracks = models.PositiveIntegerField(default=0)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True)

    gender = models.CharField(
        max_length=1, choices=(("M", "male"), ("F", "female")), blank=True, null=True
    )

    def __str__(self):
        return f"Profile {self.first_name} {self.last_name} of user {self.user_id}"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
