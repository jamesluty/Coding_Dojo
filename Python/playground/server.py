from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<string:color>')
def play_color(num=3, color="blue"):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)