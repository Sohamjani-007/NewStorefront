from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('index/', views.storage),
    path('test/', views.storage)
]