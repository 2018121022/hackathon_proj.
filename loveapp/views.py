from django.shortcuts import render, get_object_or_404, redirect
from loveapp.models import Love

# Create your views here.

def home(request):
    return render(request, 'home.html')
