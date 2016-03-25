from point import Point
class Vector(object):
    def __init__(self,point1,point2):
        self._head=Point(point1)
        self._tail=Point(point2)

    def __add__(self,other):
        x = self.point1 + other.point1
        y = self.point2 + other.point2
        return Point(x,y)







