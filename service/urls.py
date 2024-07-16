from django.urls import path
from . import views
urlpatterns = [
    path('' , views.services , name='services'),
    path('service_detail/<str:slug>' , views.service_details , name='service_details'),
    
]