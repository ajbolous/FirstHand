from dbHandler import DbHandler
from model import *

v = Vertex(12,12,12,0)
h = DbHandler('sqlite+pysqlite:///database.db')
h.add(v)
h.commit()
vert = h.vertices
verts = h.getVertex
print(vert.all())