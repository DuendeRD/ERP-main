from django.contrib import admin
from .models import Transaction, Transfer_details, Trasport, Routes

# Register your models here.


admin.site.site_header = 'Administracion de Transacciones'

admin.site.register(Transaction)
admin.site.register(Transfer_details)
admin.site.register(Trasport)
admin.site.register(Routes)
