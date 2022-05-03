from django.contrib import admin
from .models import Collection, Customer, Address


# Register your models here.

admin.site.register(Collection)
admin.site.register(Customer)
admin.site.register(Address)