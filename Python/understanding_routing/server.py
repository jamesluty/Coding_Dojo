from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/dojo')

def dojo():
    return "Dojo!"

@app.route('/say/flask')

def say_flask():
    return "Hi Flask!"

@app.route('/say/michael')

def say_michael():
    return "Hi Michael!"

@app.route('/say/john')

def say_john():
    return "Hi John!"

@app.route('/repeat/35/hello')

def repeat_hello():
    hello = ""
    for x in range(35):
        hello += "hello\n"
    return hello

@app.route('/repeat/80/bye')

def repeat_bye():
    bye = ""
    for x in range(80):
        bye += "bye\n"
    return bye

@app.route('/repeat/99/dogs')

def repeat_dogs():
    dogs = ""
    for x in range(99):
        dogs += "dogs\n"
    return dogs


if __name__=="__main__":
    app.run(debug=True)

