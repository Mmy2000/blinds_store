from django.shortcuts import render
from service.models import Services
from products.models import Blinds , Curtains , Furniture , Accessories 
from blog.models import Post
from .models import NewsLitter , Facts , OurSkills , OurRecentWork , OurClients
from django.http import JsonResponse

# Create your views here.
def home(request):
    services = Services.objects.all()
    blinds = Blinds.objects.all()[:3]
    curtains = Curtains.objects.all()[:3]
    posts = Post.objects.all()
    furnitures = Furniture.objects.all()
    facts = Facts.objects.last()
    skills = OurSkills.objects.all()
    works = OurRecentWork.objects.all()
    clients = OurClients.objects.all()
    context = {
        'services':services,
        'blinds':blinds,
        'curtains':curtains,
        'posts':posts,
        'furnitures':furnitures,
        'facts':facts,
        'skills':skills,
        'works':works,
        'clients':clients,
    }
    return render(request , 'home.html' , context )

def newsletters(request):
    email = request.POST.get('email')
    NewsLitter.objects.create(email=email)
    return JsonResponse({'done':'done'})

def custom_404_view(request, exception=None):
    return render(request, '404.html', {}, status=404)