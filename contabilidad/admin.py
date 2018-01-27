from django.contrib import admin
from .models import Pago
from .models import Proveedor
from .models import Iva

admin.site.register(Pago)
admin.site.register(Iva)
admin.site.register(Proveedor)