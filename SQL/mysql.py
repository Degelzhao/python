import pymysql

db= pymysql.connect(host="localhost",user="root",password="zxs199325",
                    db="test",port=3306)

cur = db.cursor()

sql = "select * from customer"

try:
    cur.execute(sql)

    results = cur.fetchall()
    print("customer","name","account")
    for row in results:
        customer = row[0]
        name = row[1]
        account = row[2]
        print(customer,name,account)
except Exception as e:
    raise e
finally:
    db.close()