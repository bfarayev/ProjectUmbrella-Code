from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'umbrella/index.html')

def signin(request):
    return render(request, 'umbrella/signin.html')

def register(request):
    return render(request, 'umbrella/register.html')

def googlemap(request):
    return render(request, 'umbrella/googlemap.html')
