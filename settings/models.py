from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Settings(models.Model):
    site_name = models.CharField( max_length=50)
    logo = models.ImageField( upload_to='setting/')
    phone1 = models.CharField( max_length=30)
    phone2 = models.CharField( max_length=30 , blank=True , null=True)
    email1 = models.EmailField( max_length=254)
    email2 = models.EmailField( max_length=254 ,blank=True , null=True)
    description = models.TextField(max_length=1000)
    fb_link = models.URLField( max_length=200)
    tiktok_link = models.URLField( max_length=200)
    instagram_link = models.URLField( max_length=200)
    youtube_link = models.URLField( max_length=200)
    address = models.CharField( max_length=50)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Info")

    def __str__(self):
        return self.site_name
    
class NewsLitter(models.Model):
    email = models.EmailField( max_length=254)
    created_at = models.DateTimeField(default=timezone.now)
    

    class Meta:
        verbose_name = ("NewsLitter")
        verbose_name_plural = ("NewsLitter")

    def __str__(self):
        return self.email
    
class Images(models.Model):
    title = models.CharField(_("title"), max_length=150 , help_text=_('this title is display in slider in home page'))
    settings = models.ForeignKey(Settings, related_name='home_image',verbose_name="home_image", on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    image = models.ImageField(_("image"), upload_to='homeImages/' , help_text='this image is display in slider in home page')

    class Meta:
        verbose_name = _("Home Images")
        verbose_name_plural = _("Home Images")

    def __str__(self):
        return self.title
    
class Facts(models.Model):
    clients = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()
    hours_of_support = models.PositiveIntegerField()
    hard_workers = models.PositiveIntegerField()
    image = models.ImageField(_("image"), upload_to='factImages/' )

    def __str__(self):
        return str(self.id)
    
class OurClients(models.Model):
    image = models.ImageField(_("image"), upload_to='clientImages/' )

    class Meta:
        verbose_name = _("Our Clients")
        verbose_name_plural = _("Our Clients")

    def __str__(self):
        return str(self.id)
    
class OurRecentWork(models.Model):
    image = models.ImageField(_("image"), upload_to='recentworkImages/' )

    class Meta:
        verbose_name = _("Our Recent Work")
        verbose_name_plural = _("Our Recent Work")

    def __str__(self):
        return str(self.id)
    
class OurSkills(models.Model):
    name = models.CharField(max_length=60)
    percent = models.CharField(max_length=30)


    class Meta:
        verbose_name = _("Our Skills")
        verbose_name_plural = _("Our Skills")

    def __str__(self):
        return self.name