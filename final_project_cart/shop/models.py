from django.db import models

# Create your models here.
from django.urls import reverse


class catlog(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class products(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    img= models.ImageField(upload_to='products')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(catlog,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('itemdetails',args=[self.category.slug,self.slug])


    def __str__(self):
        return '{}'.format(self.name)



