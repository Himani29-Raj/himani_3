import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float,DateTime
from sqlalchemy.ext import declarative
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
class prediction(Base):

    __tablename__ ="prediction"

    id =Column(Integer, primary_key=True)
    comment = Column(String)
    result= Column(String)
    created_on=Column(DateTime,default=datetime.now)

    def __str__(self):
        return self.comment

if __name__=="__main__":
    engine = create_engine('sqlite:///db.sqlite3')
    Base.metadata.create_all(engine)

    