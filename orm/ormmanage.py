from  orm import model
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:wang123*@localhost/flaskdb",encoding ='utf8',echo = True)

from sqlalchemy.orm import sessionmaker

session = sessionmaker()()



def insertUser(username,password):
   result= session.add(model.User(username = username,password = password))
   session.commit()
   session.close()
   print(result)

def checkUser(username,password):
    result = session.query(model.User).filter(model.User.username==username).filter(model.User.password==password).first().id

    if result:
        return result
    else:
        return -1















