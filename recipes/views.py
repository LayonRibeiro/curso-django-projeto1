from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# HTTP request
def home(request):
    # return HTTP response
    return render(request, 'recipes/home.html', context= {
        'name': 'Layon Ribeiro',
    })
        

def contact(request):
    # return HTTP response
    return render(request, 'recipes/contact.html' )
def about(request):
    # return HTTP response
    return render(request, 'recipes/about.html')