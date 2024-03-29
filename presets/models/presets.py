from django.db import models


class Preset(models.Model):

    cover = models.OneToOneField("Cover", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    scope = models.CharField(
        default="private", choices=(("private", "private"), ("public", "public")), max_length=10
    )
    file = models.FileField()
    file_type = models.CharField(
        max_length=50, choices=(("mp3", "mp3"), ("wav", "wav"))
    )
    software = models.CharField(
        max_length=50, choices=(("FL", "FrutieLoops"), ("AB", "Ableton"))
    )
    seller_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        default=0, choices=(("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))
    )
    price = models.PositiveIntegerField(default=0)
    co_authors = models.ManyToManyField("users.User", related_name="co_authors")
    created_at = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    reviews = models.ManyToManyField("Review")

    def __str__(self):
        return f"Preset {self.name}: {self.price}"

    class Meta:
        verbose_name = "Preset"
        verbose_name_plural = "Presets"


class Category(models.Model):

    name = models.CharField(max_length=50)


class Review(models.Model):

    text = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.CharField(
        max_length=1,
        choices=(("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")),
    )


class Cover(models.Model):

    # image = models.ImageField()
    pass
