from .models import Blinds , Curtains

def nav(request):
    blinds_nav = Blinds.objects.all()
    curtains_nav = Curtains.objects.all()
    context = {
        'blinds_nav':blinds_nav,
        'curtains_nav':curtains_nav
    }
    return context