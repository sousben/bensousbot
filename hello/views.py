from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def oauth(request):
    print 'new app install what else'
    print request.GET

def poll(request, pollName):
    print 'user requested poll page with name ' + pollName
    print type(request)
    print request.GET
    return render(request, 'index.html')

def db(request):
    print request
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

