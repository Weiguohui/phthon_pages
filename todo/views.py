from django.shortcuts import render

# Create your views here.

def TodoPageView(request):
    return render(request,'todo.html')
