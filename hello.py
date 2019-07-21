from flask import Flask, redirect, url_for, request, render_template
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


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello {} as guest'.format(guest)

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

@app.route('/success/<name>')
def success(name):
    return 'Welcome {}'.format(name)

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

@app.route('/html/hello/<user>/')
def index(user):
    return render_template('hello.html', name=user)


@app.route('/marks/<int:score>')
def display_marks(score):
    return render_template('marks.html', marks=score)

@app.route('/result/')
def result():
    d = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=d)

if __name__ == '__main__':
    app.run(debug=True)

