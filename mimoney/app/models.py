from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor

# Create your models here.

class Account(models.Model):
	user = models.ForeignKey(User)
	balance = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

	def __str__(self):
		return "Cuenta de " + str(self.user.first_name)

	class Meta:
		ordering = ['user']
		verbose_name = "Cuenta"
		verbose_name_plural = "Cuentas"

class Category(models.Model):
	name = models.CharField(max_length=30, default='')
	icon = fields.ImageField(upload_to='category_icon/', dependencies=[
		FileDependency(attname='icon_mini', processor=ImageProcessor(
		format='PNG', scale={'max_width': 100, 'max_height': 100})),
	])
	icon_mini = fields.ImageField(upload_to='category_icon_mini/')

	def __str__(self):
		return "Categoria " + str(self.name)

	class Meta:
		ordering = ['name']
		verbose_name = "Categoria"
		verbose_name_plural = "Categorias"

class Movement(models.Model):
	CONTRIB_CHOICES = (
		('M', 'Me'),
		('O', 'Other'),
		('B', 'Both')
	)
	TYPE_CHOICES = (
		('IN', 'Ingreso'),
		('OUT', 'Pago')
	)
	user = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
	concept = models.CharField(max_length=100, default='Concepto')
	type = models.CharField(max_length=3, choices=TYPE_CHOICES, default='OUT')
	contribution = models.CharField(max_length=1, choices=CONTRIB_CHOICES, default='M')
	done = models.BooleanField(default=False)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return str(self.concept) + ": " + str(self.amount) + " euros"

	class Meta:
		ordering = ['-date']
		verbose_name = "Movimiento"
		verbose_name_plural = "Movimientos"

class RegularPayment(models.Model):
	CONTRIB_CHOICES = (
		('M', 'Me'),
		('O', 'Other'),
		('B', 'Both')
	)
	TYPE_CHOICES = (
		('IN', 'Ingreso'),
		('OUT', 'Pago')
	)
	FREQ_CHOICES = (
		('M', 'Mensual'),
		('B', 'Bimensual'),
		('T', 'Trimestral'),
		('A', 'Anual')
	)
	user = models.ForeignKey(User)
	amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
	concept = models.CharField(max_length=100, default='Concepto')
	type = models.CharField(max_length=3, choices=TYPE_CHOICES, default='OUT')
	contribution = models.CharField(max_length=1, choices=CONTRIB_CHOICES, default='M')
	done = models.BooleanField(default=False)
	frequency = models.CharField(max_length=1, choices=FREQ_CHOICES, default='M')
	next_payment = models.DateField()

	def __str__(self):
		return str(self.concept) + ": " + str(self.amount) + " euros" + str(self.frequency)

	class Meta:
		ordering = ['-next_payment']
		verbose_name = "Pago regular"
		verbose_name_plural = "Pagos regulares"