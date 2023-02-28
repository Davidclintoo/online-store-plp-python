from django.db import models 
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False' , 'False')
    )
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    keyword = models.TextField()
    image = models.ImageField(null= True, blank= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=6)
    
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
        
    def get_url(self):
        return reverse('products_bycategory', args = [self.slug] )
    
    def __str__(self):
        return  self.name