from django.shortcuts import render
from .models import Blinds , BlindImages , Commercial , CommercialImages , Curtains , CurtainsImages , MotorizedBlinds , MotorizedBlindsImages

# Create your views here.

def blinds_list(request):
    blinds = Blinds.objects.all()
    context = {
        'blinds':blinds
    }
    return render(request , 'blinds/blinds.html' , context)

def curtains_list(request):
    curtains = Curtains.objects.all()
    context = {
        'curtains':curtains
    }
    return render(request , 'curtains/curtains.html' , context)
    
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