from .models import Blinds , Curtains , Furniture

def nav(request):
    blinds_nav = Blinds.objects.all()
    curtains_nav = Curtains.objects.all()
    furnitures_nav = Furniture.objects.all()
    context = {
        'blinds_nav':blinds_nav,
        'curtains_nav':curtains_nav,
        'furnitures_nav':furnitures_nav,
        
    }
    return context