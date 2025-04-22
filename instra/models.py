from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PosttModel(models.Model):
    nameuser = models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    photos = models.ImageField(upload_to="media/posts_images")
    description = models.TextField(max_length=150,default="Instgram_Post")
    date = models.DateTimeField(auto_now=True)


    def post_photos(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.photos.url))

