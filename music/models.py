from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True,null=True)
    details = models.CharField(max_length=50, blank=True,null=True)
    email = models.CharField(max_length=50, blank=True,null=True)
    address = models.CharField(max_length=50, blank=True,null=True)
    fav_sport = models.CharField(max_length=50, blank=True,null=True)
    content = models.TextField()
    def __str__(self):
        return self.name + ' ' + self.email

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Album(models.Model):
    artist = models.CharField(max_length=255, blank=True,null=True)
    album_title = models.CharField(max_length=255, blank=True,null=True)
    genre = models.CharField(max_length=200, blank=True,null=True)
    album_logo = models.CharField(max_length=400, blank=True,null=True)

class Song(models.Model):
    soft = models.ForeignKey(Album, on_delete=models.CASCADE)
    rock = models.CharField(max_length=255, blank=True,null=True)
    smooth = models.CharField(max_length=200, blank=True,null=True)
    instrumental = models.CharField(max_length=400, blank=True,null=True)


class Product(models.Model):
    product_name=models.CharField(max_length=255,blank=True,null=True)
    product_price=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return str(self.product_name)


