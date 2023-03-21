from django.db import models
from django.urls import reverse

# Create your models here.

# table for category
class Category(models.Model):
    name = models.CharField(max_length=250,unique=True) #category name should be unique
    slug = models.SlugField(max_length=250,unique=True) #slug will automatically create urls/links
    description = models.TextField(blank=True) #blank - true , its given to say its blank/not necessary
    image = models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self): #to create url
        return reverse('shop:products_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


# table for products
class Product(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE) # foreignkey is to link/connect 2 tables
    image = models.ImageField(upload_to='product',blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True) #true/false
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'  # name understandable by humans
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('shop:prodCatdetail',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)




