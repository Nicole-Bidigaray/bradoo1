from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    cnpj = models.CharField(max_length=18, blank=False,
                            null=False, unique=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    provider = models.ForeignKey(
        'Provider', on_delete=models.CASCADE, blank=False, related_name='product')
    name = models.CharField(max_length=150, blank=False, null=False)
    code = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
