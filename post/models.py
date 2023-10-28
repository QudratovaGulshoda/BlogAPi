from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="media/images/")
    role = models.TextField()


class Socialmedia(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="media/logos/")
    url = models.URLField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=250)
    logo = models.ImageField(upload_to="media/logos/")


class Tags(models.Model):
    title = models.CharField(max_length=250)


class Posts(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="media/post_images/")
    content = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)

    viewers = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    
    subscribe_at = models.DateTimeField(auto_now_add=True)


class Partners(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to="media/partners_logos/")
    url = models.URLField()


class Advertising(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    url = models.URLField(blank=True)
