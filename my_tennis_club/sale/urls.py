from django.urls import path
from . import views

urlpatterns = [
    path('', views.sale_view, name='sale'),
    path('cart/', views.sale_view, name='cart'),
]

