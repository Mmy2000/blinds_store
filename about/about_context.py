from .models import About

def about(request):
    about = About.objects.last()
    context = {
        'about':about,
    }
    return context