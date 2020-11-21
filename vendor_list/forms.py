from django import forms
from django.forms import ModelForm, TextInput
from .models import  Vendor_List, Product_List

#class List_Form(forms.Form):
#	text = forms.CharField(max_length=100,
#	widget=forms.TextInput(
#		attrs = {'class': 'form-control', 'placeholder': 'Insira um Item'}
#	))

#	price = forms.DecimalField(decimal_places = 2, max_digits = 20, default = 100.00,
#	widget=forms.FloatInput(
#		attrs = {'class': 'form-control', 'placeholder': 'Insira o preco'}
#	))

class Product_Form(forms.ModelForm):
	item = forms.CharField(max_length=100,
	widget=forms.TextInput(
		attrs = {'placeholder': 'Insira um Item'}
	)
	)
	description = forms.CharField(max_length=100,
	widget=forms.TextInput(
		attrs = {'placeholder': 'Insira uma descricao'}
	)
	)

	price = forms.FloatField()
	
	stock= forms.IntegerField()
	
	seller = forms.ModelChoiceField(queryset=Vendor_List.objects.all())

	class Meta:
		model = Product_List
		fields = ('item', 'description', 'price', 'stock', 'seller' )

class Product_Update(forms.ModelForm):
	class Meta:
		model = Product_List
		fields = ('item', 'description', 'price', 'stock', 'seller' )