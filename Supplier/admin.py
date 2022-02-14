from django.contrib import admin
from Supplier.models import Supplier, Orders, Orders_detail, Supplier_Contacts

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Orders)
admin.site.register(Orders_detail)
admin.site.register(Supplier_Contacts)