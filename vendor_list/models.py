from django.db import models
from django.contrib.auth.models import User

#class Post(models.Model):
#	titulo = models.CharField(max_length=100)
#	conteudo = models.TextField()
#	autor = models.ForeignKey(User, on_delete=models.CASCADE)



#	def __str__(self):
#		return self.titulo

class Vendor_List(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(default = "")

	def __str__(self):
		return self.name

class Product_List(models.Model):
	active = models.BooleanField(default=True) #quando for True vc nao pode comprar mais
	item = models.CharField(max_length=100)
	description = models.TextField(default = "")
	price = models.DecimalField(decimal_places = 2, max_digits = 20, default = 100.00)
	stock = models.IntegerField(null=True)
	seller = models.ForeignKey(Vendor_List, null=True, on_delete=models.SET_NULL,  blank=True)

	def __str__(self):
		return self.item 

	#def to_dict(self):
	#	return {"item": self.item,"description":self.description, "price": self.price,"quantidade": self.stock,"vendor": self.vendor_list}


	