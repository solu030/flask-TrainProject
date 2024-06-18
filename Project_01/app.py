from flask import Flask,render_template,request

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
        print(user,pwd)
        return 'login successful!'



@app.route('/register', methods =['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    else:
        # print(request.form)
        user = request.form.get('usr')
        pwd = request.form.get('pwd')
        gender = request.form.get('gender')
        hobby_list = request.form.getlist('hobby')
        city = request.form.get('city')
        skill_list = request.form.getlist('skill')
        more = request.form.get('more') 
        print(user,pwd,gender,hobby_list,city,skill_list,more)
        return 'register successful!'

if __name__ == '__main__':
    app.run()