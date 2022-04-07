from ast import Num
from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/dojo')

def dojo():
    return "Dojo!"

@app.route('/say/<string:flask>')

def say_flask(flask):
    return f"Hi {flask}!"

@app.route('/say/<string:michael>')

def say_michael(michael):
    return f"Hi {michael}!"

@app.route('/say/<string:john>')

def say_john(john):
    return f"Hi {john}!"

@app.route('/repeat/<int:num>/hello')

def repeat_hello(num):
    hello = ""
    for x in range(num):
        hello += "hello\n"
    return hello

@app.route('/repeat/<int:num>/bye')

def repeat_bye(num):
    bye = ""
    for x in range(num):
        bye += "bye\n"
    return bye

@app.route('/repeat/<int:num>/dogs')

def repeat_dogs(num):
    dogs = ""
    for x in range(num):
        dogs += "dogs\n"
    return dogs


if __name__=="__main__":
    app.run(debug=True)

