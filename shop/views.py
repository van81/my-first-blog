from django.shortcuts import render
from shop.models import Shop,Good,Seller

def all_shops(request):
  shops = Shop.objects.all()
  return render(request, 'shop/post_list.html', {'shops': shops})

def all_goods(request):
  goods = Good.objects.all()
  return render(request, 'shop/post_list.html', {'goods': goods})

def all_sellers(request):
  shops = Seller.objects.all()
  return render(request, 'shop/post_list.html', {'sellers': sellers})

def shops_conatins(request):
  for shop in Shop.objects.all():
    