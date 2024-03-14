from django.urls import path
from display import views

urlpatterns = [
    path("", views.home, name="home"),
    path("insert", views.insert_coin, name="insert_coin"),
    path("return", views.coin_return, name="coin_return"),
    path("dispense", views.dispense_product, name="dispense_product"),
]