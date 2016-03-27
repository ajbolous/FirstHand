class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        p = Point(self.x + other.x, self.y + other.y, self.z + other.z)
        return p

    def __sub__(self, other):
        q = Point(self.x - other.x, self.y - other.y, self.z - other.z)
        return q

    def __str__(self):
        return "point <{} , {} , {}>".format(self.x, self.y, self.z)
