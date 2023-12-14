from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    return render(request,'display_topic.html',d)

def display_webpages(request):
    QLTO=Webpage.objects.all()
    d={'webpage':QLTO}
    
    return render(request,'display_webpages.html',d)

