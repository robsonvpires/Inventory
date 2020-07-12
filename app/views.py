from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Item, Sala, Category

# Create your views here.
def index(request):
    context = {
        'items': Item.objects.all(),
        'salas': Sala.objects.all(),
        'categorys': Category.objects.all(),
        'users': User.objects.all()
    }
    return render(request, 'app/index.html', context)