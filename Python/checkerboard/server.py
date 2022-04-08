from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<int:row>')
@app.route('/<int:row>/<int:col>')
@app.route('/<int:row>/<int:col>/<string:row_color>/<string:column_color>')
def checkerboard(row=8, col=8, row_color="red", column_color="black"):
    return render_template("index.html", row=row, col=col, row_color=row_color, column_color=column_color)

if __name__=="__main__":
    app.run(debug=True)