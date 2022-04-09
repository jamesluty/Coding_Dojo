from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "this is a secret key"

@app.route('/')
def index():
    show_button = ""
    output = ""
    attempts = 0
    show_tries = ""

    if session.get('number') is None:
        session['number'] = random.randint(1,100)
        session['attempts'] = attempts
    print(session['number'])

    if 'guess' in session:
        if int(session['guess']) == int(session['number']):
            output = "Correct"
            show_button = "flex"
            session['attempts'] += 1
        elif int(session['guess']) > int(session['number']):
            output = "Too high"
            session['attempts'] += 1
            show_tries = "flex"
        else:
            output = "Too low"
            session['attempts'] += 1
            show_tries = "flex"

    if session['attempts'] == 5:
        output = "You lose!"
        show_button = "flex"
    return render_template("index.html", tries=show_tries, output_text=output, button=show_button, attempts=session['attempts'])

@app.route('/guess', methods=['POST'])
def make_guess():
    session['guess'] = request.form['number']
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)