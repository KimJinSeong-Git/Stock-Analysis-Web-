from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("야호!")

def create(request):
    return HttpResponse('만들어!')

def read(request, id):
    return HttpResponse('나는: ' + id)