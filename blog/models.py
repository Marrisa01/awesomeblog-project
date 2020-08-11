from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    image = models.ImageField(upload_to="blog_images/")
    text = models.TextField()
