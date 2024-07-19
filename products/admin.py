from django.contrib import admin
from .models import Blinds, BlindImages, Commercial, CommercialImages, Curtains, CurtainsImages, MotorizedBlinds, MotorizedBlindsImages , Furniture , FurnitureImages , Category , Accessories , AccessoriesImages
from django_summernote.admin import SummernoteModelAdmin
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class BlindGallaryInline(admin.TabularInline):
    model = BlindImages
    extra = 1

@admin_thumbnails.thumbnail('image')
class CommercialGallaryInline(admin.TabularInline):
    model = CommercialImages
    extra = 1

@admin_thumbnails.thumbnail('image')
class CurtainsGallaryInline(admin.TabularInline):
    model = CurtainsImages
    extra = 1

@admin_thumbnails.thumbnail('image')
class MotorizedBlindsGallaryInline(admin.TabularInline):
    model = MotorizedBlindsImages
    extra = 1

@admin_thumbnails.thumbnail('image')
class FurnitureGallaryInline(admin.TabularInline):
    model = FurnitureImages
    extra = 1

@admin_thumbnails.thumbnail('image')
class AccessoriesGallaryInline(admin.TabularInline):
    model = AccessoriesImages
    extra = 1



class BlindsModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    inlines = [BlindGallaryInline]

class MotorizedBlindsModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    inlines = [MotorizedBlindsGallaryInline]

class CommercialModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    inlines = [CommercialGallaryInline]

class CurtainsModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    inlines = [CurtainsGallaryInline]

class FurnitureModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    inlines = [FurnitureGallaryInline]

class AccessoriesModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    inlines = [AccessoriesGallaryInline]



admin.site.register(Blinds, BlindsModelAdmin)
admin.site.register(BlindImages)
admin.site.register(Commercial, CommercialModelAdmin)
admin.site.register(CommercialImages)
admin.site.register(Curtains, CurtainsModelAdmin)
admin.site.register(CurtainsImages)
admin.site.register(MotorizedBlinds, MotorizedBlindsModelAdmin)
admin.site.register(MotorizedBlindsImages)
admin.site.register(Furniture , FurnitureModelAdmin)
admin.site.register(FurnitureImages)
admin.site.register(Category)
admin.site.register(Accessories , AccessoriesModelAdmin)
admin.site.register(AccessoriesImages)