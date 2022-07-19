from django.urls import path, include
from likes import views

# from rest_framework.routers import SimpleRouter, DefaultRouter

urlpatterns = [
    path('get_excel/', views.GetShowExcelApiView.as_view()),
    path('read_excel/', views.ShowExcelApiView.as_view()),  
]



