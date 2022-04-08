from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    count = 1
    session['count'] += count
    return render_template("index.html", count=session['count'])

@app.route('/count')
def add_one():
    session['count'] += 1
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    session['count']=0
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)