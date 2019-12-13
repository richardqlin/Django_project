from django.urls import path

from . import views


app_name='oenstopshop'

urlpatterns = [
    path('', views.onestopshop, name='onestopshop'),
    path('buy', views.buy, name='buy'),
    path('add', views.add, name='add'),

    path('checkout', views.checkout, name ='checkout'),
]