from flask import render_template, redirect, request, session
from flask_app.models.model_user import User
from flask_app.models.model_message import Message
from flask_app import app

@app.route("/wall")
def welcome():
    context = {
        'all_users': User.get_all(),
        'messages': Message.get_messages_for_user({'id': session['uuid']}),
        'counter': Message.get_message_count({'id': session['uuid']}),
        'other_users': User.get_others({'id': session['uuid']}),
        'sent_count': session['sent_counter']
    }

    if 'uuid' in session:
        user = User.login_user({'id': session['uuid']})
        context['user'] = user
    return render_template("wall.html", **context)

@app.route("/delete/<int:id>")
def delete(id):
    print(id)
    Message.delete_message({'id': id})
    return redirect("/wall")