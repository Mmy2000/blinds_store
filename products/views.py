from django.shortcuts import render
from .models import Blinds , BlindImages , Commercial , CommercialImages , Curtains , CurtainsImages , MotorizedBlinds , MotorizedBlindsImages

# Create your views here.

def blinds_list(request):
    blinds = Blinds.objects.all()
    context = {
        'blinds':blinds
    }
    return render(request , 'blinds/blinds.html' , context)

def blinds_details(request , slug):
    blinds_detail = Blinds.objects.get(slug=slug)
    context = {
        'blinds_detail':blinds_detail
    }
    return render(request , 'blinds/blinds_details.html' , context)

def curtains_list(request):
    curtains = Curtains.objects.all()
    context = {
        'curtains':curtains
    }
    return render(request , 'curtains/curtains.html' , context)

def curtains_details(request , slug):
    curtains_detail = Curtains.objects.get(slug=slug)
    context = {
        'curtains_detail':curtains_detail
    }
    return render(request , 'curtains/curtains_details.html' , context)
    
def commercial_list(request):
    commercial = Commercial.objects.last()
    context = {
        'commercial':commercial
    }
    return render(request , 'commercial/commercial.html' , context)


def motorizedblinds(request):
    motorizedblind = MotorizedBlinds.objects.last()
    context = {
        'motorizedblind':motorizedblind
    }
    return render(request , 'motorizedblind/motorizedblind.html' , context)