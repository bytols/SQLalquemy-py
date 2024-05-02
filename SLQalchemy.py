import sqlalchemy
from sqlalchemy import Column, Integer , String , ForeignKey
from sqlalchemy.orm import declarative_base , relationship
from sqlalchemy.orm import DeclarativeBase

base = declarative_base()

class User(base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column (String)

    address = relationship(
        'Adress' , back_populates='user' , cascade='all , delete-orphan'
    )

    def __repr__(self):
        return f'usario é: id:{self.id} , nome: {self.name} e nome complete: {self.fullname}'  

class Address(base):
    id = Column(Integer , primary_key =True , autoincrement = True)
    email_adress = Column(String(30))
    user_id = Column(Integer, ForeignKey('user_account.id') , nullable = False)

    user = relationship(
        'User' , back_populates= 'address' , cascade='all , delete-orphan'
    )

    def __repr__ (self):
        return f" id{self.id} , Email {self.email_adress}" 
    
print(User.id)