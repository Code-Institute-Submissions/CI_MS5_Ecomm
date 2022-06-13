from django import forms

from .models import Product, Inventory


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['slug',]
        widgets = {
            'holding': forms.CheckboxSelectMultiple,
        }



class InventoryModelForm(forms.ModelForm):
    class Meta:
        model = Inventory
        exclude = ['size', 'color', 'product',]