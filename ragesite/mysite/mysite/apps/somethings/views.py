from django.shortcuts import render

def index(request):
    return render(request, 'somethings/list.html')
