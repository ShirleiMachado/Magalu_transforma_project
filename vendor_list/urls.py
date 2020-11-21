"""magalu_transforma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from.import views

urlpatterns = [
    path('', views.home, name='vendor_list-home'), 
    path('about/', views.about, name='vendor_list-about'),
    path('courses/', views.courses, name='vendor_list-courses'),    
    path('products/', views.index, name='vendor_list-index'),
	path('add/', views.add_new_item, name='vendor_list-add'),
    path('update/', views.update_product, name='vendor_list-update'),
	path('see_all/', views.see_all, name='vendor_list-see_all'),
	path('inactive_item/<int:item_id>/', views.inactive_item, name='vendor_list-inactive'),
	#path('delete_all/', views.delete_all, name='vendor_list-delete_all'),
]
		
