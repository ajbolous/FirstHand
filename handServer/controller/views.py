from django.http import HttpResponse
from handControl.hand import  *
# Create your views here.

def move(request):
    hand.move([120,120,100,200])
    return HttpResponse('you requested me ')
