from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page
from django.http import HttpResponseRedirect, JsonResponse
from .models import *


def about(request):

    return render(request, 'about.html')

def home(request):
    category = Category.objects.all()

    context = {
        'category': category
    }
    return render(request, 'index.html', context)

def privacy(request):

    return render(request, 'privacy.html')


def contact(request):

    return render(request, 'contact.html')


def product(request, category, id):
    cat = Category.objects.get(id=id)
    post = Product.objects.filter(category=cat)

    context = {
        'post': post
    }

    return render(request, 'product.html', context)


def post_detail(request, name, pk):
    post = Product.objects.get(pk=pk)

    context = {
        'post': post
    }

    return render(request, 'post-details.html', context)


def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)


def error_500(request):
    data = {}
    return render(request, '500.html', data)