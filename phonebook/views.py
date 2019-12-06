from django.shortcuts import render, redirect, get_object_or_404
#from django.views.decorators.csrf import csrf_exempt
from django.http import *

from .forms import PhoneForm

from .models import Phonebook

# Create your views here.

def phonebook(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/phonebook')
    else:
        form = PhoneForm()
        forms = Phonebook.objects.all()
    return render(request, 'phonebook/phonebook.html', {'form': form, 'forms':forms})

def display(request):
    form = Phonebook.objects.all()
    return render(request, 'phonebook/display.html', {'form': form})

def delete(request,id):
    obj = get_object_or_404(Phonebook,id=id)
    print(obj, request.method)

    #if request.method == 'POST':
    if obj is not None:
        obj.delete()
        return redirect('/phonebook')

    form = Phonebook.objects.all()
    return render(request,'phonebook/deleted.html',{'form':form})





