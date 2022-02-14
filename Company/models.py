from django.db import models
#from Users.models import User
from simple_history.models import HistoricalRecords

class Company(models.Model):
    name = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

class DistributionCenter(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Centros de Distribución'
