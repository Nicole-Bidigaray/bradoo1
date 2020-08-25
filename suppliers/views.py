from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Provider, Product
from rest_framework import status

from .forms import ProviderForm, ProductForm


def home(request):
    context = {'mensagem': 'Olá mundo...'}
    return render(request, 'suppliers/index.html', context)


def list_providers(request):
    providers = Provider.objects.all()
    form = ProviderForm()
    data = {'providers': providers, 'form': form}
    return render(request, 'suppliers/list_providers.html', data)


def provider_new(request):
    form = ProviderForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('suppliers_list_providers')


def provider_update(request, id):
    data = {}
    provider = Provider.objects.get(id=id)
    form = ProviderForm(request.POST or None, instance=provider)
    data['provider'] = provider
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('suppliers_list_providers')
    else:
        return render(request, 'suppliers/update_provider.html', data)


def provider_delete(request, id):
    provider = Provider.objects.get(id=id)
    if request.method == 'POST':
        provider.delete()
        return redirect('suppliers_list_providers')
    else:
        return render(request, 'suppliers/delete_confirm.html', {'obj': provider})


def list_products(request):
    products = Product.objects.all()
    form = ProductForm()
    data = {'products': products, 'form': form}
    return render(request, 'suppliers/list_products.html', data)


def product_new(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('suppliers_list_products')


def product_update(request, id):
    data = {}
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    data['product'] = product
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('suppliers_list_products')

    else:
        return render(request, 'suppliers/update_product.html', data)


def product_delete(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('suppliers_list_products')
    else:
        return render(request, 'suppliers/delete_confirm.html', {'obj': product})
