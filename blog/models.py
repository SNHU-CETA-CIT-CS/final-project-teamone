from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

