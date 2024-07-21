from django.contrib import admin
from .models import Settings , NewsLitter , Images , Facts , OurClients , OurRecentWork , OurSkills
# Register your models here.
admin.site.register(Settings)
admin.site.register(NewsLitter)
admin.site.register(Images)
admin.site.register(Facts)
admin.site.register(OurClients)
admin.site.register(OurRecentWork)
admin.site.register(OurSkills)