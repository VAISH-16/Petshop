from .models import Orders
from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields="__all__"
        exclude=['order_id','user','paid']