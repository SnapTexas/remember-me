from sqlalchemy import Column , Integer, String 
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Login(Base):
    __tablename__="Login-credentials"

    username = Column(String,unique= True , primary_key= True,index= True)
    password = Column(String)


class signup(Base):
    __tablename__="Signup-credentials"
    username = Column(String,unique= True , primary_key= True)
    password = Column(String)
    email = Column(String,unique= True )

