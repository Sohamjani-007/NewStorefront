from django.contrib import admin
from django.http import HttpResponse
from .models import Album, Product, Song, Contact, MyModel
import xlwt
from .views import export_xlsx


# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artist', 'album_title', 'genre', 'album_logo')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('soft', 'rock', 'smooth', 'instrumental')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'details','email', 'address', 'fav_sport', 'content')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price')


class MyModelAdmin(admin.ModelAdmin):
    actions = [export_xlsx]
    list_display = ('title', 'description')
admin.site.register(MyModel, MyModelAdmin)
