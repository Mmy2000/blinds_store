from django.shortcuts import render
from service.models import Services
from products.models import Blinds , Curtains
# Create your views here.
def home(request):
    services = Services.objects.all()[:4]
    blinds = Blinds.objects.all()[:3]
    curtains = Curtains.objects.all()[:3]
    context = {
        'services':services,
        'blinds':blinds,
        'curtains':curtains
    }
    return render(request , 'home.html' , context )