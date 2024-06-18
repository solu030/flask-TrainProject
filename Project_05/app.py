from flask import Flask,render_template,request
import pymysql

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    else:
        user = request.form.get('username')
        pwd = request.form.get('password')
        mobile = "111111111"
        print(user,pwd)

        return 'login successful!'



@app.route('/register', methods =['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    else:
        # print(request.form)
        user = request.form.get('usr')
        mob = request.form.get('mob')
        pwd = request.form.get('pwd')
        gender = request.form.get('gender')
        hobby_list = request.form.getlist('hobby')
        city = request.form.get('city')
        skill_list = request.form.getlist('skill')
        more = request.form.get('more') 
        print(user,pwd,gender,hobby_list,city,skill_list,more)
        # xxxxxxxxxxxxxxxxxxxxxxxxxxx
        conn = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",password = "12345",db ="unicom")
        cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)

        sql="insert into admin(username,password,mobile) values(%s,%s,%s)"
        cursor.execute(sql,[user,pwd,mob])
        conn.commit()

        cursor.close()
        conn.close()

        # xxxxxxxxxxxxxxxxxxxxxxxxxx
        return 'register successful!'

@app.route('/show')
def show():
    conn = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",password = "12345",db ="unicom")
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)

    sql="select * from admin "
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)

    cursor.close()
    conn.close()
    return render_template('show.html',data_list = res)

if __name__ == '__main__':
    app.run()