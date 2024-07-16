from django.urls import path
from . import views
urlpatterns = [
    path('blinds/' , views.blinds_list , name='blinds_list'),
    path('curtains/' , views.curtains_list , name='curtains_list'),
    path('commercial/' , views.commercial_list , name='commercial_list'),
    path('motorizedblind/' , views.motorizedblinds , name='motorizedblinds'),
]