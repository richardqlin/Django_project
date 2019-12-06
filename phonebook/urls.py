from django.urls import path

from . import views

app_name='phonebook'
urlpatterns = [
    path('', views.phonebook, name='phonebook'),
    path('display',views.display, name = 'display'),
    path('delete/<int:id>',views.delete, name = 'delete'),
]