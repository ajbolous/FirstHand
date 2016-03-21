from django.shortcuts import render
from django.http import HttpResponse
from FirstHand.python.hand import Hand
# Create your views here.

def move(request):
    h = Hand()
    print(h)
    return HttpResponse('you requested me ')