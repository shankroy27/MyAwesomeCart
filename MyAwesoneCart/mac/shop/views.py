from django.shortcuts import render
from django.http import HttpResponse
from .models import product , Contact , orders , OrderUpdate
from math import ceil
import json

# Create your views here.

def index(request):
    # prod = product.objects.all()
    allprods = []
    catprods = product.objects.values('category' , 'id')
    cats = {item['category'] for item in catprods }
    # print(cat)
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1 , nSlides) , nSlides])
    # params = {'no_of_slides' : nSlides , 'products': prod , 'range': range(1,nSlides)}
    params = {'allprods':allprods}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,"shop/About.html")

def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank = True
    return render(request,"shop/contact.html",{'thank':thank})

def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid','')
        email = request.POST.get('email','')
        try:
            order = orders.objects.filter(order_id=orderid,email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                print(update)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc , 'time':item.timestamp})
                    #print(updates)
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
                return HttpResponse('{}')
    return render(request,"shop/tracker.html")


def search(request):
    return render(request, "shop/search.html")

def productview(request,myid):
    prod = product.objects.filter(id=myid)
    return render(request,"shop/prodView.html" , {'prod':prod[0]})

def checkout(request):
    if request.method == "POST":
        items_json=request.POST.get('itemjson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address1','') +" " +request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
        thank = True
        order = orders(items_json=items_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
        idu = order.order_id
        update = OrderUpdate(order_id=order.order_id, update_desc="Your order has been placed")
        update.save()
        return render(request,"shop/checkout.html",{'thank':thank ,'idu': idu})
    return render(request,"shop/checkout.html")
