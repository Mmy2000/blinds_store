from .models import Services

def service_footer(request):
    services_footer = Services.objects.all()[:4]
    context = {
        'services_footer':services_footer
    }
    return context