import pymysql

conn = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",password = "12345",db ="unicom")
cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)

# username = input("请输入新用户名:")
# password = input("请输入新密码:")
# mobile = input("请输入新手机号:")

sql="update admin set mobile = %s where id = %s"
cursor.execute(sql,["5555555","1"])
conn.commit()

cursor.close()
conn.close()