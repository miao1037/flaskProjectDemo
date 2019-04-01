"""
ORM：o用于生成数据库中的表
"""





class Book():

    def __init__(self,_id,_name,_price):
        self.id = _id
        self.name = _name
        self.price = _price


    def __str__(self):
        return "id:%s name:%s price: %s"%(self.id,self.name,self.price)

from sqlalchemy import  create_engine

engine = create_engine("mysql+mysqlconnector://root:wang123*@localhost/flaskdb",encoding ='utf8',echo = True)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(bind=engine)

from  sqlalchemy import  Column,Integer,String

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    username = Column(String(20),nullable=False)
    password = Column(String(50),nullable=False)


if __name__=='__main__':

    #创建表  必须卸载main模块
    Base.metadata.create_all(bind=engine)


    # print(engine)





















