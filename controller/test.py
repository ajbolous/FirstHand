from hand import Hand
from vector import Vector
from point import Point
#h = Hand()
#h.move([134,123,34,34])
#for i in range (0,4):
   # line = h._serial._serial.readline()
    #print(line)

v = Vector([0,0,1],[0,0,0])
print(v._head._coords,v._tail._coords)

p1=Point([0,0,0])

p2=Point([1,1,1])
print(p1._coords+p2._coords)