from django.shortcuts import redirect,render
from django.http import HttpResponse
from lists.models import Item,List
# Create your views here.


def home_page(request):
    return render(request,'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request,'list.html',{'items':items})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'items': items})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})