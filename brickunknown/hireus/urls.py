from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="hireus"),
    path("cart/",views.cart,name="cart"),
    path("checkout/",views.checkout,name="checkout"),
]
