from flask import Flask
from flask import request

webapp = Flask(__name__)                             # 实例化一个Flask应用

@webapp.route('/', methods = ['GET', 'POST'])        # 添加首页URL
def home():
    return '<h1>Home</h1>'

@webapp.route('/signin', methods = ['GET'])          # 添加登陆页URL,用于GET请求
def signin_from():
    return '''<form action="/signin" method="post">
                  <p><input name="username"></p>
                  <p><input name="password" type="password"></p>
                  <p><button type="submit">Sign In</button></p>
                  </form>'''

@webapp.route('/signin', methods = ['POST'])         # 添加登陆页URL,用于POST请求
def signin():
    if request.form['username'] == 'Degel' and request.form['password'] == 'zxs199325':
        return '<h3> Hello, Degel!</h3>'
    return '<h3>Bad username or password,</h3>'

if __name__ == '__main__':
    webapp.run()

