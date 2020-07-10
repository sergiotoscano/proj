from django.shortcuts import render
from django.http import HttpResponse

def homeview(request):
    return render(request, 'home/index.html', context=None)


def baseview(request):
    return render(request, 'home/base.html', context=None)    