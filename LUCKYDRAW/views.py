from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
    return render(request,'LUCKYDRAW/home.html')
def about(request):
    return render(request,'LUCKYDRAW/about.html')
def homee(request):
    return render(request,'LUCKYDRAW/homee.html')
def service(request):
    return render(request,'LUCKYDRAW/services.html')