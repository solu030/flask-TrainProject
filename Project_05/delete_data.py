import pymysql

conn = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",password = "12345",db ="unicom")
cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)

id = input("请输入要删除用户的id:")

sql="delete from admin where id = (%s)"
cursor.execute(sql,[id])
conn.commit()

cursor.close()
conn.close()