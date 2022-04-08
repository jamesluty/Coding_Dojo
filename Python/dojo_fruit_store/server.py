from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    apple_count = request.form['apple']
    raspberry_count = request.form['raspberry']
    strawberry_count = request.form['strawberry']
    count = apple_count + raspberry_count + strawberry_count

    print(f"Charging {first_name} {last_name} for {count} fruits")

    return render_template("checkout.html")

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)