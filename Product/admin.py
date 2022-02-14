from django.contrib import admin
from .models import Product, Inventory, Assigned, Equipment_warranty, Defect

# Register your models here.
admin.site.site_header = 'Administracion de Productos'

admin.site.register(Product)
admin.site.site_title = 'Administracion de Productos'
admin.site.index_title = 'Productos'
admin.site.register(Inventory)
admin.site.register(Assigned)
admin.site.register(Equipment_warranty)
admin.site.register(Defect)


