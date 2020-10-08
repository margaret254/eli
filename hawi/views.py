from django.shortcuts import render
from .models import Posts,Clients

# Create your views here.

def home(request):
    img = Posts.objects.all()
    corp = Posts.objects.filter(category="corporate")
    sport = Posts.objects.filter(category="sports")
    wedding = Posts.objects.filter(category="weddings")
    doc = Posts.objects.filter(category="documentaries")
    logo = Clients.objects.all()
    return render(request, 'index.html', {"img":img,"corp":corp,"sport":sport,"wedding":wedding,"doc":doc,"logos":logo})




