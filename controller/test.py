from hand import Hand
from vector import Vector
from point import Point
from Geometry  import Geometry
#h = Hand()
#h.move([134,123,34,34])
#for i in range (0,4):
   # line = h._serial._serial.readline()
    #print(line)
p1=Point(1,1,1)
p2=Point(3,3,3)
p3=Point(4,4,4)
p4=Point(7,7,7)
v1 = Vector(p1,p2)
v2=Vector(p3,p4)
#print(v1._head)
#print(v1._tail)
#print(p2-p1)
#print(p1+p2)
#print(v1._head+v2._tail)
print(v1+v2)
g=Geometry(v1)
print(g._distance(v1))