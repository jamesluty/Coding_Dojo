from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "this is a secret key"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    location = request.form['location']
    course = request.form['course']
    language = request.form['language']
    comments = request.form['comments']
    checkbox = request.form['checkbox']
    return render_template('results.html', course=course, checkbox=checkbox, name=name, location=location, language=language, comments=comments)


if __name__=="__main__":
    app.run(debug=True)