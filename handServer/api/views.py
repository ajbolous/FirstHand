from django.http import HttpResponse
import handControl.hand
# Create your views here.

def move(request):
    handControl.hand.hand.move([120,120,100,150])
    return HttpResponse('you requested me ')
