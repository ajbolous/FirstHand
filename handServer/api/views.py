from django.http import HttpResponse

from handControl.hand import *
import random


# Create your views here.

def move(request):
   x=int(request.GET['x'])
   y=int(request.GET['y'])
   z=int(request.GET['z'])
   w=int(request.GET['w'])
   hand.move([x,y,z,w])
   return HttpResponse('you requested : {}, {}, {}, {}'.format(x,y,z,w))
