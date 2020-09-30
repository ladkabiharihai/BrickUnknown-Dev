from django.urls import path
from . import views
from hireus.models import Product

urlpatterns = [
    path("",views.index,name="hireus"),
    path("bookorder/",views.bookorder,name="bookorder"),
    path("booked/",views.Booked,name="booked"),
    path("products/<int:Product_id>",views.productview,name="productview"),
]
