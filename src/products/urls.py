from django.urls import path

from . import views

urlpatterns = [
	path('detail/', views.product_detail_view),
	path('create/', views.product_create_view),
   
]