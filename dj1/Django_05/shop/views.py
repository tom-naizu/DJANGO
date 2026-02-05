from django.shortcuts import render

def product(request):
    return render(request,'shop/product.html')
