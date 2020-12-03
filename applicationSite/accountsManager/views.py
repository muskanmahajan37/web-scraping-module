from django.shortcuts import render

# Create your views here.

def mainProfile(request):
    return render(request, 'name.html')