
from django.db import models
from django.contrib.auth.models import User

from simple_history.models import HistoricalRecords

from Product.models import Product

# Create your models here.

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    RNC = models.CharField(max_length=50, unique=True)
    phone = models.CharField(("Phone number"), blank=True, max_length=20)
    Address = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    Country = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplier_created_by', editable=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Proveedores'
        verbose_name_plural = 'Proveedores'



class Orders (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_created_by')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ordenes'
        verbose_name_plural = 'Ordenes'

class Orders_detail (models.Model):
    id = models.AutoField(primary_key=True)
    ID_Order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ID_Product = models.ForeignKey(Product, on_delete=models.Case, related_name='Producto', default=None)
    Quantity = models.CharField(max_length=50)
    Price= models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_detail_created_by')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Detalle de Ordenes'
        verbose_name_plural = 'Detalle de Ordenes'


class Supplier_Contacts (models.Model):
    id = models.AutoField(primary_key=True)
    ID_Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(("Phone number"), blank=True, max_length=20)
    Address = models.CharField(max_length=50, blank=True)
    Email = models.EmailField(max_length=254, blank=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplier_contact_created_by')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Contactos de Proveedores'
        verbose_name_plural = 'Contactos de Proveedores'
