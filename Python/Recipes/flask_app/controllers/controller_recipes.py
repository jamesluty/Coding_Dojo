from flask_app import app, bcrypt
from flask import render_template, redirect, request, session
from flask_app.models.model_recipe import Recipe
from flask_app.models.model_user import User


# create recipe
@app.route("/create/recipe")
def create():
    return render_template("add_recipe.html")

# add recipe
@app.route("/add/recipe", methods=['POST'])
def add():
    user_id = session['uuid']
    data = {
        **request.form,
        'user_id': user_id
    }

    Recipe.add_recipe(data)
    return redirect("/dashboard")

# show recipe
@app.route("/recipes/<int:id>")
def show_recipe(id):
    user = User.get_user({'id':session['uuid']})
    recipe = Recipe.show_recipe({'id':id})
    return render_template("view_recipe.html", recipe=recipe, user=user)

# edit recipe
@app.route("/recipes/edit/<int:id>")
def edit_recipe(id):
    recipe = Recipe.show_recipe({'id':id})
    return render_template("edit_recipe.html", recipe=recipe)

@app.route("/update/recipe/<int:id>", methods=['POST'])
def update_recipe(id):
    data = {
        **request.form,
        'recipe_id': id
    }

    Recipe.update_recipe(data)
    return redirect("/dashboard")

@app.route("/delete/<int:id>")
def delete_recipe(id):
    Recipe.delete_recipe({'id':id})
    return redirect("/dashboard")