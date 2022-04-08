from flask import Flask, render_template

app = Flask(__name__)

@app.route('/list')
def list():
    studentsInfo = [
        {'first' : 'Michael', 'last' : 'Choi'},
        {'first' : 'John', 'last' : 'Supsupin'},
        {'first' : 'Mark', 'last' : 'Guillen'}
    ]
    return render_template('index.html', students=studentsInfo)

if __name__=="__main__":
    app.run(debug=True)