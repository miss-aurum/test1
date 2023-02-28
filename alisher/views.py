from django.shortcuts import render
from .models import * 

def take(request):
    context = {'news': News.objects.all()}
    return render(request, 'alisher/alisher.html', context)



# Create your views here.
