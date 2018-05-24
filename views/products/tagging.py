from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views import View
from shop.models import Product, ProductTag, Tag

class TaggingProducts:
    def post(self, request):
        products_ids = request.POST['products']
        tags_ids = request.POST['tags']
        tags = Tag.objects.filter(pk__in=tags_ids)
        products = Product.objects.filter(pk__in=products_ids)