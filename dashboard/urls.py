from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.home, name='home'),
    path('staff/', views.staff, name='staff'),
    path('products/', views.products, name='products'),
    path('products/delete/<int:pk>', views.products_delete, name='products_delete'),
    path('products/update/<int:pk>', views.products_update, name='products_update'),
    path('order/', views.order, name='order'),
]
