from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    if session.get('count') is None:
        count = 1
        session['count'] = count
    return render_template("index.html", count=session['count'])

@app.route('/count')
def add_one():
    session['count'] += 1
    return redirect('/')

@app.route('/two')
def add_two():
    session['count'] += 2
    return redirect('/')

@app.route('/input', methods=['POST'])
def add_input():
    amount = request.form['amount']
    session['count'] += int(amount)
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)