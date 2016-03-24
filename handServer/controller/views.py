from FirstHand.python.hand import Hand
from django.http import HttpResponse


# Create your views here.

def move(request):
    h = Hand()
    print(h)
    return HttpResponse('you requested me ')
