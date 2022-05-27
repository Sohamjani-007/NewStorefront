from django.urls import path
from . import views

urlpatterns = [
    path('userregistration/', views.showformdata),
    path('productregistration/', views.product_data),
    path('music/excel_home', views.export_abc_xlsx, name='export_excel'),

]
