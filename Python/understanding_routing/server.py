from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following

def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

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


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

