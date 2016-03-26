class Point(object):
    def __init__(self,x,y,z):
       self._x = x
       self._y = y
       self._z = z


    def __add__(self,other):
        p = Point(self._x + other._x, self._y + other._y , self._z + other._z)
        return p
    def __sub__(self,other):
        q = Point(self._x - other._x, self._y - other._y , self._z - other._z)
        return q


    def __str__(self):
        return "point <{} , {} , {}>".format(self._x,self._y , self._z)

