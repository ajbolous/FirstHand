import math

def distance(p1, p2):
    dist = math.pow((p2.x - p1.x),2) + math.pow((p2.y - p1.y),2) + math.pow((p2.z - p1.z),2)
    return math.sqrt(math.fabs(dist))