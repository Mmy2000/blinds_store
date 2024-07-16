from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class ModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(About,ModelAdmin)