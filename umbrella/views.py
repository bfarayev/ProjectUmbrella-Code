from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'umbrella/index.html')

def signin(request):
    return render(request, 'umbrella/signin.html')

def googlemap(request):
    return render(request, 'umbrella/googlemap.html')
