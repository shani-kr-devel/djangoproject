from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')
def contact(request):
    return render(request, 'website/contact.html')
def about(request):
    return render(request, 'website/about.html')
def help(request):
    return render(request, 'website/help.html')
