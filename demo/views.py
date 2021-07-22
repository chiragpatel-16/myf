from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   ##  return HttpResponse("<h1>hi hello <h1>")
   return render(request, 'home.html', {'name': 'chirag patel'})


def add(request):
    no1 = int(request.GET['num1'])
    no2 = int(request.GET['num2'])
    res = no1 + no2
    return render(request, 'result.html', {'result': res})