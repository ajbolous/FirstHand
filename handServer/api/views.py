from django.http import HttpResponse

from handControl.hand import *


# Create your views here.

def move(request):
    hand.move([int(request.GET['x']),
               int(request.GET['y']),
               int(request.GET['z']),
               int(request.GET['w'])
               ])
    return HttpResponse('you requested me ')
