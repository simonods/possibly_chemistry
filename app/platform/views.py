from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home_view(request):
    return render(request, 'home.html', {"now": datetime.now()})

def dynamic_message(request):
    return HttpResponse("Це динамічне повідомлення з HTMX!")
