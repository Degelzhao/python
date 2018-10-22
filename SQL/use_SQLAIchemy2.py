from sqlalchemy import Column, String, create_engine, Integer, MetaData, Table
from sqlalchemy.orm import sessionmaker, relationship, mapper
from sqlalchemy.ext.declarative import declarative_base

# 创建实例，并连接test库
engine = create_engine('mysql+pymysql://root:zxs199325@localhost:3306/test')

#元数据
metadata = MetaData()

Customer = Table('Customer', metadata,
                 Column('cust', Integer, primary_key = True),
                 Column('name', String(20)),
                 Column('account', String(18))
            )

class User(object):
    def __init__(self):
        self.cust = cust
        self.name = name
        self.account = account

    def __repr__(self):
        output = "(%s,%s,%s)" %(self.cust,self.name,self.account)
        return output

mapper(User, Customer)

session_class = sessionmaker(bind=engine)
session = session_class()
info1 = session.query(User).filter(User.cust == 1).one()    # filter相等用‘==’
info2 = session.query(User).filter_by(cust = 2).one()       # filter_by相等用‘=’
info3 = session.query(User).filter(User.cust > 5).all()
print(info1,info2,info3)

#多条件查询:
obj = session.query(User).filter(User.cust > 2).filter(User.cust < 5).all()
print(obj)
