from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base,Vertex

class DbHandler(object):
    def __init__(self, db_url):
        self._url = db_url
        self._engine = create_engine(self._url)
        Session = sessionmaker(bind=self._engine)
        self._session = Session()

    @property
    def vertices(self):
        return self._session.query(Vertex).all()

    def add(self, obj):
        self._session.add(obj)

    def commit(self):
        self._session.commit()

    def create_tables(self):
        Base.metadata.ccreate_all(self._engine)