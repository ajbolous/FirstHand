import geometry

class Vector(object):
    def __init__(self, point1, point2):
        self._head = point1
        self._tail = point2
        self._len = geometry.distance(point1, point2)

    def __str__(self):
        return "<vector {} >".format(self._tail-self._head)

    def __add__(self, other):
        v = Vector(self._head, other._tail)
        return v
