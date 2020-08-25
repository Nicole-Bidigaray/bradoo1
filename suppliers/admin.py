from django.contrib import admin
from .models import Provider, Product


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'city')
    list_filter = ('id', 'name', 'cnpj')
    search_fields = ('id', 'name', 'cnpj', 'city')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'provider', 'price')
    list_filter = ('name', 'code', 'price')
    search_fields = ('name', 'code', 'provider', 'price')


admin.site.register(Provider, ProviderAdmin)
admin.site.register(Product, ProductAdmin)
