from sqlalchemy import Float,Integer,Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vertex(Base):
    __tablename__ = 'vertices'

    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    o = Column(Float)

    def __init__(self,x, y, z, o):
        self.x = x
        self.y = y
        self.z = z
        self.o = o

    def __repr__(self):
        return "Vertex[{}]({},{},{},{})".format(self.id,self.x,self.y,self.z,self.o)

