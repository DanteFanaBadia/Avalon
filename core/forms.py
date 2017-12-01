from django.forms import ModelForm
from suit.widgets import EnclosedInput, LinkedSelect


from . import models


class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        fields = ('number', 'due_date', 'ship_date', 'customer', 'employee')
        widgets = {
            'customer': LinkedSelect,
        }


class OrderDetailForm(ModelForm):
    class Meta:
        model = models.OrderDetail
        fields = ('number', 'order', 'part', 'quantity')
        widgets = {
            'part': LinkedSelect,
            'quantity': EnclosedInput(prepend='#'),
        }


class PartForm(ModelForm):
    class Meta:
        model = models.Part
        fields = ('number', 'name', 'price', 'quantity')
        widgets = {
            'price': EnclosedInput(prepend='RD$', append='.00'),
        }
