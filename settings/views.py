from django.shortcuts import render
from service.models import Services
from products.models import Blinds , Curtains , Furniture , Accessories
from blog.models import Post
from .models import NewsLitter
from django.http import JsonResponse

# Create your views here.
def home(request):
    services = Services.objects.all()[:4]
    blinds = Blinds.objects.all()[:3]
    curtains = Curtains.objects.all()[:3]
    posts = Post.objects.all()
    furnitures = Furniture.objects.all()
    context = {
        'services':services,
        'blinds':blinds,
        'curtains':curtains,
        'posts':posts,
        'furnitures':furnitures,
    }
    return render(request , 'home.html' , context )

def newsletters(request):
    email = request.POST.get('email')
    NewsLitter.objects.create(email=email)
    return JsonResponse({'done':'done'})