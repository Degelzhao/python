#SQLAIchemy中一对多实例:
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine

# 创建实例，并连接test库
engine = create_engine('mysql+pymysql://root:zxs199325@localhost:3306/test')
# 生成ORM基类
Base = declarative_base()

class Stu(Base):
    __tablename__ = 'student'                #表名
    id = Column(Integer,primary_key = True)
    name = Column(String(20))

    #使查询结果变为可读，而非映射
    def __repr__(self):
        output = "(%s,%s)" %(self.id,self.name)
        return output

class Score(Base):
    __tablename__ = 'score'
    sid = Column(Integer,primary_key = True,autoincrement = True)
    math_score = Column(Integer)
    chinese_score = Column(Integer)
    english_score = Column(Integer)
    student = Column(Integer, ForeignKey('student.id'))

    #使查询结果变为可读，而非映射
    def __repr__(self):
        output = "(%s,%s,%s,%s)" %(self.id,self.math_score,self.chinese_score,self.english_score)
        return output

# 创建表结构(这里是父类调子类)
Base.metadata.create_all(engine)
# 创建与数据库的会话session class,返回DBSession的class
DBSession = sessionmaker(bind=engine)    #绑定实例
# 生成session实例，相当于游标
session = DBSession()
# 添加分数数据
session.add_all([
    Score(math_score = 85,chinese_score = 87,english_score = 90,student = 1)
    #Score(chinese_score = 87, student = 1),
    #Score(english_score = 90, student = 1)
])
# 提交
session.commit()
# 关闭连接
session.close()