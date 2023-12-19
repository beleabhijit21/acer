from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        labels ={
            'oid':'ORDER ID',
            'product':'PRODUCT NAME',
            'quantity':'QUANTITY',
            'price':'PRICE',
            'del_date':'DELIVERY DATE',
            'address':'ADDRESS',
            'phone':'PHONE',
            'mail':'E-mail id'
        }
        
        widgets = {
            'del_date': forms.DateInput(attrs={'type':'date'}),
            'address': forms.Textarea()
        }