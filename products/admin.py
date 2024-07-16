from django.contrib import admin
from .models import Blinds , BlindImages , Commercial , CommercialImages , Curtains , CurtainsImages , MotorizedBlinds , MotorizedBlindsImages
# Register your models here.

admin.site.register(Blinds)
admin.site.register(BlindImages)
admin.site.register(Commercial)
admin.site.register(CommercialImages)
admin.site.register(Curtains)
admin.site.register(CurtainsImages)
admin.site.register(MotorizedBlinds)
admin.site.register(MotorizedBlindsImages)