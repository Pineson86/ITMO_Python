import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Модель таблицы
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    group = Column(String, name='"group"')
#Соединение
engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:1231@localhost/university_db')

Base.metadata.create_all(engine)

#Функция для создания курсора
def curs():
    session = sessionmaker(bind=engine)
    return session()
