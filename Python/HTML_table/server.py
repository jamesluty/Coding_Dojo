from flask import Flask, render_template

app = Flask(__name__)

@app.route('/list')
def list():
    studentsInfo = [
        {'first' : 'James', 'last' : 'Luty'},
        {'first' : 'Obi', 'last' : 'Wan'},
        {'first' : 'Darth', 'last' : 'Vader'}
    ]
    return render_template('index.html', students=studentsInfo)

if __name__=="__main__":
    app.run(debug=True)