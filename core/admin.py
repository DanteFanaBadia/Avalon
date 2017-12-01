from django.contrib import admin
from django.contrib.auth import get_user_model

from . import models
from . import forms


class EmployeeAdmin(admin.ModelAdmin):
    list_display_links = ('number', 'first_name', 'last_name', 'zip_code')
    list_display = ('number', 'first_name', 'last_name', 'zip_code')


class CustomerAdmin(admin.ModelAdmin):
    list_display_links = ('number', 'first_name', 'last_name', 'zip_code')
    list_display = ('number', 'first_name', 'last_name', 'zip_code')


class PartAdmin(admin.ModelAdmin):
    form = forms.PartForm
    list_display_links = ('number', 'name', 'price', 'quantity')
    list_display = ('number', 'name', 'price', 'quantity')
    search_fields = ('name',)


class OrderInline(admin.TabularInline):
    raw_id_fields = ('part',)
    model = models.OrderDetail
    extra = 5
    form = forms.OrderDetailForm


class OrderAdmin(admin.ModelAdmin):
    list_display_links = ('number', 'due_date', 'ship_date', 'customer', 'employee',)
    list_display = (
        'number',
        'due_date',
        'ship_date',
        'customer',
        'employee',
    )
    raw_id_fields = ('customer', 'employee')
    form = forms.OrderForm
    inlines = [OrderInline, ]
    list_filter = ('due_date', 'ship_date', 'customer', 'employee', )
    search_fields = ('customer__first_name', 'employee__first_name', 'employee__last_name', 'customer__last_name')


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Employee, EmployeeAdmin)
_register(models.Customer, CustomerAdmin)
_register(models.Part, PartAdmin)
_register(models.Order, OrderAdmin)
