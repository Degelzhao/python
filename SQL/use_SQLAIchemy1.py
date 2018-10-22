from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建实例，并连接test库
engine = create_engine('mysql+pymysql://root:zxs199325@localhost:3306/test')
# 生成ORM基类
Base = declarative_base()

class User(Base):
    __tablename__ = 'Customer'           #表名
    cust = Column(Integer, primary_key=True)
    name = Column(String(20))
    account = Column(Integer)

    #使查询结果变为可读，而非映射
    def __repr__(self):
        output = "(%s,%s,%s)" %(self.cust,self.name,self.account)
        return output

# 创建表结构(这里是父类调子类)
Base.metadata.create_all(engine)
# 创建与数据库的会话session class,返回DBSession的class
DBSession = sessionmaker(bind=engine)    #绑定实例
# 生成session实例，相当于游标
session = DBSession()
# 查询
my_cust = session.query(User).filter(User.cust == 3).one()          #filter()表示条件，one()表示返回唯一行
print(my_cust)
# 生成你要创建的数据对象
new_cust = User(cust = 6, name = 'Elvis', account = 700000000)
# 把创建的数据对象添加到session里
session.add(new_cust)
# 创建提交
session.commit()
# 打印结果
print(new_cust.cust,new_cust.name,new_cust.account)
# 关闭数据库连接
session.close()

