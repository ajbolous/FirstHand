from point import Point
class Vector(object):
    def __init__(self,point1,point2):
        self._head=point1
        self._tail=point2
        self.v=self._tail-self._head
    def __str__(self):
        return "vector< {} >".format(self.v)


    def __add__(self,other):
        t=self.v+other.v
        return t
















