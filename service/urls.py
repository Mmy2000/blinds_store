from django.urls import path
from . import views
urlpatterns = [
    path('' , views.services , name='services'),
    path('<str:slug>' , views.service_details , name='service_details'),
    
]