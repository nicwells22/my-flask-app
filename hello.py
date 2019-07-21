from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hello')
def hello_world2():
    return 'Hello World2'

def hello_world3():
    return 'Hello World3'
app.add_url_rule('/','hello3',hello_world3)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello {}!'.format(name)

@app.route('/hello/<int:i>')
def multi_hello(i):
    return 'Hello World!<br>' * i

@app.route('/hello/<float:f>')
def float_hello(f):
    return 'Hello World<br>Float Value: {}'.format(f)

@app.route('/<str1>/<str2>')
def test_multi_param(str1,str2):
    return '{} {}'.format(str1,str2)


@app.route('/<int:id>/hello/')
def test_reverse(id):
    return 'This page id is: {}<br>Hello Visitor!'.format(id)





if __name__ == '__main__':
    app.run(debug=True)

