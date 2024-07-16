from django.shortcuts import render

from .models import Services
# Create your views here.
def services(request):
    services = Services.objects.all()
    context = {
        'services':services
    }
    return render(request , 'services.html' , context)

def service_details(request,slug):
    service_detail = Services.objects.get(slug=slug)
    context = {
        'service_detail':service_detail
    }
    return render(request , 'service_detail.html' , context)