from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Preset(models.Model):

    cover = models.OneToOneField("Cover", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    scope = models.BooleanField()
    file = models.FileField()
    file_type = models.CharField(
        max_length=50, choices=(("mp3", "mp3"), ("wav", "wav"))
    )
    software = models.CharField(
        max_length=50, choices=(("FL", "FrutieLoops"), ("AB", "Ableton"))
    )
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    co_authors = models.ManyToManyField(User, related_name='co_authors')
    created_at = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    reviews = models.ManyToManyField("Review")

    class Meta:
        verbose_name = "Preset"
        verbose_name_plural = "Presets"


class Category(models.Model):

    name = models.CharField(max_length=50)


class Review(models.Model):

    text = models.TextField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.CharField(
        max_length=1,
        choices=(("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")),
    )


class Cover(models.Model):

    file_path = models.FilePathField(
        default="defualt file path"
    )  # Add default file path
