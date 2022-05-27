from django.contrib import admin
from .models import Album, Product, Song, Contact

# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artist', 'album_title', 'genre', 'album_logo')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('soft', 'rock', 'smooth', 'instrumental')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'content')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price')