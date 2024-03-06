from django.db import models


class Preset(models.Model):

    cover = models.OneToOneField("Cover", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    scope = models.BooleanField()
    file = models.FileField()
    file_type = models.Choices((("mp3", "mp3"), ("wav", "wav")))
    software = models.Choices((("FL", "FrutieLoops"), ("AB", "Ableton")))
    seller_id = models.ForeignKey("User", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    co_authors = models.ManyToManyField("User")
    created_at = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    reviews = models.ManyToManyField("Review")


class Category(models.Model):

    name = models.CharField(max_length=50)


class Review(models.Model):

    text = models.TextField()
    author_id = models.ForeignKey("User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.Choices((("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")))


class Cover(models.Model):

    preset_id = models.OneToOneField("Preset", on_delete=models.CASCADE)
    file_path = models.FilePathField(
        default="defualt file path"
    )  # Add default file path
