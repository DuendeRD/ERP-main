from django.db import models

from simple_history.models import HistoricalRecords

from Company.models import DistributionCenter
from Users.models import Employees


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, default='Producto')
    Models = models.CharField(max_length=100, default='Modelo')
    Serial = models.CharField(unique=True, max_length=50)
    IMEI = models.CharField(unique=True, max_length=50)
    Descriptions = models.CharField('Descriptión', blank=True, max_length=500)
    Type = models.CharField(max_length=50, default='Tipo',
    choices=[('Phone', 'Phone'), 
            ('Tablet', 'Tablet'), 
            ('Accessory', 'Accessory'),
            ('Printer', 'Printer'),
            ('Scanner', 'Scanner'),
            ('Laptop', 'Laptop'),
            ('Desktop', 'Desktop'),
            ('Monitor', 'Monitor'),
            ('Software', 'Software'),
            ('Other', 'Other')
        ]
    
    )
    history = HistoricalRecords()
    Status = models.CharField(max_length=50,
    choices=[('Functional', 'Averiado')], default='Functional')
       

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'

"""
class Product_Type(models.Model):
    ID_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Tipos de Productos'
        verbose_name_plural = 'Tipos de Productos'"""


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    ID_Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ID_DistributionCenter = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('ID_Product',)
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'


class Assigned (models.Model):
    id = models.AutoField(primary_key=True)
    ID_Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ID_DistributionCenter = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE)
    ID_Employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Asignado'
        verbose_name_plural = 'Asignados'

class Equipment_warranty (models.Model):
    ID_Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ID_DistributionCenter = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE)
    Warranty_date_end = models.DateField(default='2020-01-01', blank=True, null=True, verbose_name='Fecha de vencimiento')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Garantía'
        verbose_name_plural = 'Garantías'

class Defect (models.Model):
    ID_Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ID_DistributionCenter = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE)
    Defect_description = models.CharField(max_length=500, blank=True, null=True,verbose_name="Descripción")
    Defect_date = models.DateField(default='2020-01-01', blank=True, null=True, verbose_name='Fecha de avería')
    Defect_time = models.TimeField(default='00:00:00', blank=True, null=True, verbose_name='Hora de avería')
    Defect_status = models.CharField(max_length=50,
    choices=[('Functional', 'Averiado'), ('Defective', 'Defectuoso')], default='Functional')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Avería'
        verbose_name_plural = 'Averías'
