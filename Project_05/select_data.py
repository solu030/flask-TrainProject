import pymysql

conn = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",password = "12345",db ="unicom")
cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)

id = input("请输入要查找用户的id:")

sql="select * from admin where id = %s"
cursor.execute(sql,[id])
res = cursor.fetchall()
print(res)

cursor.close()
conn.close()