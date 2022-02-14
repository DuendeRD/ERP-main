from django.contrib import admin

from Supplier.models import Orders, Orders_detail, Supplier, Supplier_Contacts
from .models import Company, DistributionCenter

# Register your models here.

admin.site.register(Company)
admin.site.register(DistributionCenter)

