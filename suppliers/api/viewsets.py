from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from suppliers.models import Provider
from .serializers import ProviderSerializer
from rest_framework import mixins
from rest_framework.decorators import action
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class ProviderViewSet(ModelViewSet):
    serializer_class = ProviderSerializer
    filter_fields = ('id', 'name', 'cnpj')
    lookup_field = 'id'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        cnpj = self.request.query_params.get('cnpj', None)
        product = self.request.query_params.get('product', None)
        queryset = Provider.objects.all()

        if id:
            queryset = Provider.objects.filter(pk=id)
        if name:
            queryset = queryset.filter(name=name)
        if cnpj:
            queryset = queryset.filter(cnpj=cnpj)
        if product:
            queryset = queryset.filter(product=product)
        return queryset

    def list(self, request, *args, **kwargs):
        return super(ProviderViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(ProviderViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ProviderViewSet, self).destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ProviderViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ProviderViewSet, self).partial_update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ProviderViewSet, self).retrieve(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
