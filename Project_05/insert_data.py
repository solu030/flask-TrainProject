import pymysql

conn = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",password = "12345",db ="unicom")
cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)

username = input("请输入用户名:")
password = input("请输入密码:")
mobile = input("请输入手机号:")

sql="insert into admin(username,password,mobile) values(%s,%s,%s)"
cursor.execute(sql,[username,password,mobile])
conn.commit()

cursor.close()
conn.close()