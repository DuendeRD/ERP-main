
from datetime import datetime
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

from simple_history.models import HistoricalRecords

from Company.models import Company, DistributionCenter
from Product.models import Product

# Create your models here.

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    DistributionCenter_out = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE, related_name='Salida')
    DistributionCenter_in = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE, related_name='Entrada')
    Estatus = models.CharField(max_length=50, default='Pendiente envio')
    
    STATUS_CHOICES = (
        ('A', 'En transito'),
        ('P', 'Pendiente Envio'),
        ('C', 'Cancelado'),
        ('E', 'Entregado'),        
        ('E', 'Entregado'),
    )
    history = HistoricalRecords()
    Created_by = models.ForeignKey( User, on_delete=models.CASCADE, editable=False, related_name='transaction_created_by')
    Comment = models.CharField(max_length=500)

    def __str__(self):
        return self.Estatus

    def save(self, *args, **kwargs):
        if not self.id:
            self.Created_by = User.objects.get(id=1)
        return super(Transaction, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Transaccion'
        verbose_name_plural = 'Transacciones'


class Transfer_details (models.Model):
    id = models.AutoField(primary_key=True)
    Transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfer_created_by')
    history = HistoricalRecords()
    Comment = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.Product.name + ' ' + str(self.Quantity)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Detalle de Transferencia'
        verbose_name_plural = 'Detalles de Transferencia'

class Trasport (models.Model):
    id = models.AutoField(primary_key=True)
    Transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Name_Transport = models.CharField(max_length=100)
    Code_ID_transport = models.CharField(max_length=100)
    Phone = models.CharField(("Numero de telefono"),max_length=50, blank=True)
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transport_created_by')
    history = HistoricalRecords()
    Comment = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.Company.name

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Transporte'
        verbose_name_plural = 'Transportes'

class meta:
    ordering = ('-created_at',)
    verbose_name = 'Transporte'
    verbose_name_plural = 'Transportes'


class Routes (models.Model):
    id = models.AutoField(primary_key=True)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Name_Route = models.CharField(max_length=100)
    Code_ID_Route = models.CharField(max_length=100)
    Phone = models.CharField(("Numero de telefono"),max_length=50, blank=True)
    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='route_created_by')
    history = HistoricalRecords()
    Comment = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.Company.name, self.Name_Route

    
    class Meta:
        ordering = ('Name_Route',)
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'


        
        
        
        