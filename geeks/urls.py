from django.urls import path
from . import views
# importing views from views.py


urlpatterns = [
	path('userregistration/', views.export_data),
	path('geeks_event/', views.geeks_show),

]


