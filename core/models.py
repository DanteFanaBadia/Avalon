from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    number = models.AutoField('Numero', primary_key=True)
    first_name = models.CharField('Nombre', max_length=200)
    last_name = models.CharField('Apellido', max_length=200)
    zip_code = models.CharField('Zip Code', max_length=200)

    def __str__(self):
        return '%s - %s %s' % (self.number, self.first_name, self.last_name)


class Customer(models.Model):
    class Meta:
        verbose_name = 'Clientes'
        verbose_name_plural = 'Clientes'
    number = models.AutoField('Numero', primary_key=True)
    first_name = models.CharField('Nombre', max_length=200)
    last_name = models.CharField('Apellido', max_length=200)
    zip_code = models.CharField('Zip Code', max_length=200)

    def __str__(self):
        return '%s - %s %s' % (self.number, self.first_name, self.last_name)


class Part(models.Model):
    class Meta:
        verbose_name = 'Parte'
        verbose_name_plural = 'Partes'
    number = models.AutoField('Numero', primary_key=True)
    name = models.CharField('Nombre', max_length=200)
    price = models.DecimalField('Precio', decimal_places=2, max_digits=18, null=True, blank=True)
    quantity = models.IntegerField('Cantidad')

    def __str__(self):
        return '%s - %s' % (self.number, self.name)


class Order(models.Model):
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
    number = models.AutoField('Numero', primary_key=True)
    customer = models.ForeignKey(Customer, verbose_name='Cliente')
    due_date = models.DateField('Fecha Realizacion')
    ship_date = models.DateField('Fecha Envio')
    employee = models.ForeignKey(Employee, verbose_name='Empleado')

    def __str__(self):
        return '%s - %s' % (self.number, self.customer)


class OrderDetail(models.Model):
    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'
    number = models.AutoField('Numero', primary_key=True)
    order = models.ForeignKey(Order, verbose_name='Orden')
    part = models.ForeignKey(Part, verbose_name='Parte')
    quantity = models.IntegerField('Cantidad')

    def __str__(self):
        return '%s - %s - %s' % (self.order, self.part, self.quantity)