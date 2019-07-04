from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

from .forms import *


def index(request):
    return render(request, 'inv/index.html')

def display_inventario(request):
    items = Inventario.objects.all()
    context = {
        'items': items,
        'header': 'Items',
    }
    return render(request, 'inv/index.html', context)

