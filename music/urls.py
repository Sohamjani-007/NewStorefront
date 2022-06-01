from django.urls import path
from . import views, admin

urlpatterns = [
    path('userregistration/', views.showformdata),
    path('my_model/', views.export_xlsx),
    path('product_registration/', views.product_data),

]
