from django.shortcuts import render
from .models import Blinds , BlindImages , Commercial , CommercialImages , Curtains , CurtainsImages , MotorizedBlinds , MotorizedBlindsImages , Furniture , Accessories

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
    curtains = Curtains.objects.last()
    context = {
        'curtains':curtains
    }
    return render(request , 'curtains/curtains_details.html' , context)

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

def furniture_list(request):
    furnitures = Furniture.objects.all()
    context = {
        'furnitures':furnitures
    }
    return render(request , 'furnitures/furnitures.html' , context)

def furniture_details(request , slug):
    furniture_details = Furniture.objects.get(slug=slug)
    context = {
        'furniture_details':furniture_details
    }
    return render(request , 'furnitures/furniture_details.html' , context)

def accessory_list(request):
    accessories = Accessories.objects.last()
    context = {
        'accessories':accessories
    }
    return render(request , 'accessories/accessories.html' , context)
