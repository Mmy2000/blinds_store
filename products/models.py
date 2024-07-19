from django.db import models
from django.utils import timezone
from django.utils.text import slugify 
# Create your models here.

class Blinds(models.Model):
    title = models.CharField(max_length=5000)
    description = models.TextField(("description"),max_length=100000)
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    image = models.ImageField(upload_to='blinds/')
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Blinds,self).save(*args,**kwargs)

    class Meta:
        verbose_name = ("Blinds")
        verbose_name_plural = ("Blinds")

    def __str__(self):
        return self.title
    
class BlindImages(models.Model):
    blind = models.ForeignKey(Blinds,related_name='blind_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blindimages/')

    class Meta:
        verbose_name = ("Blind Images")
        verbose_name_plural = ("Blind Images")

    def __str__(self):
        return str(self.blind)
    
class Curtains(models.Model):
    title = models.CharField(max_length=5000)
    description = models.TextField(("description"),max_length=100000)
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    image = models.ImageField(upload_to='curtains/')
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Curtains,self).save(*args,**kwargs)

    class Meta:
        verbose_name = ("Curtains")
        verbose_name_plural = ("Curtains")

    def __str__(self):
        return self.title
    
class CurtainsImages(models.Model):
    curtains = models.ForeignKey(Curtains,related_name='curtains_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='curtainsimages/')

    class Meta:
        verbose_name = ("Curtains Images")
        verbose_name_plural = ("Curtains Images")

    def __str__(self):
        return str(self.curtains)


class MotorizedBlinds(models.Model):
    title = models.CharField(max_length=5000)
    description = models.TextField(("description"),max_length=100000)
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    image = models.ImageField(upload_to='motorized-blinds/')
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(MotorizedBlinds,self).save(*args,**kwargs)

    class Meta:
        verbose_name = ("MotorizedBlinds")
        verbose_name_plural = ("MotorizedBlinds")

    def __str__(self):
        return self.title
    
class MotorizedBlindsImages(models.Model):
    motorizedblinds = models.ForeignKey(MotorizedBlinds,related_name='motorizedblinds_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='motorizedblindsimages/')

    class Meta:
        verbose_name = ("MotorizedBlinds Images")
        verbose_name_plural = ("MotorizedBlinds Images")

    def __str__(self):
        return str(self.motorizedblinds)
    
class Commercial(models.Model):
    title = models.CharField(max_length=5000)
    description = models.TextField(("description"),max_length=100000)
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    image = models.ImageField(upload_to='commercial/')
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Commercial,self).save(*args,**kwargs)

    class Meta:
        verbose_name = ("Commercial")
        verbose_name_plural = ("Commercial")

    def __str__(self):
        return self.title
    
class CommercialImages(models.Model):
    commercial = models.ForeignKey(Commercial,related_name='commercial_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='commercialimages/')

    class Meta:
        verbose_name = ("Commercial Images")
        verbose_name_plural = ("Commercial Images")

    def __str__(self):
        return str(self.commercial)
    

class Furniture(models.Model):
    title = models.CharField(max_length=5000)
    description = models.TextField(("description"),max_length=100000)
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    image = models.ImageField(upload_to='Furniture/')
    slug = models.SlugField(null=True,blank=True)
    category = models.ForeignKey("Category",related_name="furniture_category", verbose_name=("Furniture Category"), on_delete=models.CASCADE)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Furniture,self).save(*args,**kwargs)

    class Meta:
        verbose_name = ("Furnitures")
        verbose_name_plural = ("Furnitures")

    def __str__(self):
        return self.title
    
class FurnitureImages(models.Model):
    furniture = models.ForeignKey(Furniture,related_name='furniture_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='furnitureimages/')

    class Meta:
        verbose_name = ("Furniture Images ")
        verbose_name_plural = ("Furniture Images ")

    def __str__(self):
        return str(self.furniture)

    
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Furniture Category")
        verbose_name_plural = ("Furniture Category")

    def __str__(self):
        return self.name
    

    
class Accessories(models.Model):
    title = models.CharField(max_length=5000)
    description = models.TextField(("description"),max_length=100000)
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    image = models.ImageField(upload_to='accessories/')
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Accessories,self).save(*args,**kwargs)

    class Meta:
        verbose_name = ("Accessories")
        verbose_name_plural = ("Accessories")

    def __str__(self):
        return self.title

class AccessoriesImages(models.Model):
    accessories = models.ForeignKey(Accessories,related_name='accessories_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accessoriesimages/')

    class Meta:
        verbose_name = ("Accessories Images ")
        verbose_name_plural = ("Accessories Images ")

    def __str__(self):
        return str(self.accessories)