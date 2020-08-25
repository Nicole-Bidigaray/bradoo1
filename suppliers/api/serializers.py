from rest_framework.serializers import ModelSerializer
from suppliers.models import Provider, Product
from rest_framework import serializers
# from html_json_forms.serializers import JSONFormSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'code', 'price']


class ProviderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Provider
        fields = ['id', 'name', 'cnpj', 'city', 'product']
