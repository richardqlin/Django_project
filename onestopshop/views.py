from django.shortcuts import render,redirect

from .forms import OneStopShopForm

from .models import OneStopShop


def onestopshop(request):
    return render(request,'onestopshop/home.html')


def add(request):
    print (request.method,request.POST)
    if request.method == 'POST':
        form = OneStopShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/onestopshop/add')
    else:
        form = OneStopShopForm()
    return render(request, 'onestopshop/add.html', {'form': form})

def buy(request):
    forms = OneStopShop.objects.all().values()
    lst = []
    for i in forms:
        doc = {}
        print(i,i['quantity'])
        doc['title'] = i['title']
        doc['description'] = i['description']
        doc['unit'] = i['unit']
        doc['price'] = i['price']
        doc['image'] = i['image']
        doc['quantity'] = range(1,i['quantity']+1)
        lst.append(doc)
    context = {'forms':lst}
    if request.method == 'POST':
        form = dict(request.POST)
        request.session['user'] = form
        return redirect('/onestopshop/checkout')
    else:
        return render(request,'onestopshop/buy.html',context)


def checkout(request):
    form = request.session['user']
    forms = OneStopShop.objects.all().values()
    #print(form)
    #print(forms)
    total = 0
    lst = []
    for i in forms:
        doc = {}
        doc['title']=i['title']
        doc['price'] = i['price']
        doc['quantity'] = i['quantity']
        if i['title'] in form:
            price = i['price']
            qty = int(form[i['title']][0])
            doc['unit'] = qty
            item = price*qty
            doc['total']=item
            #print(price,qty,item)

            total += item
        lst.append(doc)
    print(lst)

    return render(request,'onestopshop/checkout.html',{'form':lst,'total':total})

