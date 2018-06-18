from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    my_vars = {
        'banter': 'You\'re actually bald'
    }
    return render(request, 'index.html', my_vars)

def about(request):
    text = request.GET['mytext']
    my_vars = {
        'printit': text.split()
    }
    return render(request, 'about.html', my_vars)

def test(request):
    return HttpResponse('<h1>Hello World!</h1>')