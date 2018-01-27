from django.db import models
from django.utils import timezone
from django.conf import settings


class Proveedor(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)
	nit = models.CharField(max_length=30)

class Iva(models.Model):
	descripcion = models.CharField(max_length=200)
	porcentaje = models.IntegerField( )

class Pago(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	descripcion = models.CharField(max_length=200)
	factura_proveedor = models.CharField(max_length=20)
	fecha_gasto = models.DateTimeField(
	        default=timezone.now)
	valor_neto = models.DecimalField(max_digits=20, decimal_places=2)
	valor_bruto = models.DecimalField(max_digits=20, decimal_places=2)
	monto_iva = models.DecimalField(max_digits=20, decimal_places=2)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	iva = models.ForeignKey(Iva, on_delete=models.CASCADE)

	def __str__(self):
		return self.descripcion

