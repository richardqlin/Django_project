from django.urls import path

from . import views

app_name='jumbleword'

urlpatterns = [

    path('jumble',views.jumble,name='jumble'),

    path('', views.frontpage, name='frontpage'),
    path('findout', views.findout, name='findout'),
    path('clear/', views.clear, name='clear'),
]