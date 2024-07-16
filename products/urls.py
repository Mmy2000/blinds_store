from django.urls import path
from . import views
urlpatterns = [
    path('blinds/' , views.blinds_list , name='blinds_list'),
    path('blinds/<str:slug>' , views.blinds_details , name='blinds_details'),
    path('curtains/' , views.curtains_list , name='curtains_list'),
    path('curtains/<str:slug>' , views.curtains_details , name='curtains_details'),
    path('commercial/' , views.commercial_list , name='commercial_list'),
    path('motorizedblind/' , views.motorizedblinds , name='motorizedblinds'),
]