from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from.forms import Product_Form, Product_Update
from.models import Vendor_List, Product_List


def index(request):
	products = Product_List.objects.all().order_by('item')
	product_form = Product_Form()
	context = (
		{'product_form': product_form, 'products':products}
	)
	return render(request,'vendor_list/index.html',context)

def see_all(request):
	products = Product_List.objects.all().order_by('item')
	return render(request, 'vendor_list/see_all.html',{'products':products})

@require_POST
def add_new_item(request):
	product_form = Product_Form(request.POST)
	
	if product_form.is_valid():
		product_form.save()
	return redirect('vendor_list-index')

def update_product(request,id):
	instance = Product_Form.objects.get(pk=id)
	product_form = Product_Update(request.POST or None, instance = instance)

	if product_form.is_valid():
		product_form.save()
	return redirect('vendor_list-index')

def inactive_item(request,item_id):
	product = Product_List.objects.get(pk=item_id) #pk é primary key pq é a posição do item
	product.active = False
	product.save()
	return redirect('vendor_list-index')

#def delete_item(request):
#	Product_List.objects.filter(active__exact=True).delete()
#	return redirect('vendor_list-index')

#def delete_all(request):
#	Vendor_List.objects.all().delete()
#	return redirect('vendor_list-index')

def home(request):
	return render(request, "vendor_list/home.html")

def about(request):
	return render(request, "vendor_list/about.html")

