from django import forms
from .models import Product, Supplier, SaleOrder, StockMovement

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = '__all__'

class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = '__all__'
