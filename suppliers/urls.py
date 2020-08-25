from django.conf.urls import url, include
from .views import (
    home,
    list_providers,
    provider_new,
    provider_update,
    provider_delete,
    list_products,
    product_new,
    product_update,
    product_delete
)


urlpatterns = [
    url(r'^$', home, name='suppliers_home'),

    url(r'^providers/$', list_providers, name='suppliers_list_providers'),
    url(r'^provider-new/$', provider_new, name='suppliers_provider_new'),
    url(r'^provider-update/(?P<id>\d+)/$',
        provider_update, name='suppliers_provider_update'),
    url(r'^provider-delete/(?P<id>\d+)/$',
        provider_delete, name='suppliers_provider_delete'),


    url(r'^products/$', list_products, name='suppliers_list_products'),
    url(r'^product-new/$', product_new, name='suppliers_product_new'),
    url(r'^product-update/(?P<id>\d+)/$',
        product_update, name='suppliers_product_update'),
    url(r'^product-delete/(?P<id>\d+)/$',
        product_delete, name='suppliers_product_delete'),
]
