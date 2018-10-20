import os
import sqlite3

db_file = os.path.join(os.path.dirname(__file__), r'C:\Users\asd\PycharmProjects\python\test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

# 返回指定分数区间的名字，并且按照分数从小到大排序
def get_score(low, high):

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

    # 检测错误
    except sqlite3.DatabaseError as err:
        print(err)
    else:
        # 拿取数据并排序
        cursor.execute('select * from user where score >= ? and score <= ? order by score', (low, high))
        data = cursor.fetchall()
        # 返回只包含name的一个list
        return list(map(lambda x:x[1],data))
    finally:
        cursor.close()
        conn.commit()
        conn.close()

# 测试
print ('接下来为调试部分\n')
print ('调试开始-----------》\n')
assert get_score(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print ('调试结束-----------》\n')

res1 = get_score(60, 100)
res2 = get_score(60, 70)
res3 = get_score(70, 80)


# 小结:
# SQLite是一种嵌入式数据库，由C编写，体积小，可以集成到各种应用中，Python内置了SQLite,可以直接使用
# 在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据
# 要确保打开的Connection对象和Cursor对象都正确的关闭，否则，资源就会泄露
# 可以使用try:...except:...finally:...来确保出错的情况下也关闭掉Connection对象和Cursor对象
