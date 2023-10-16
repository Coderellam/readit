from django.db import models
from django.contrib import admin


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    is_solved = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    author_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, )
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


