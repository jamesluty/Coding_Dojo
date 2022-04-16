from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.model_survey import Survey


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    survey = Survey.get_last()
    print(survey)
    return render_template('results.html', survey=survey)

@app.route('/add/survey', methods=['POST'])
def add_survey():

    is_valid = Survey.validate_survey(request.form)
    if not is_valid:
        return redirect('/')

    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'course': request.form['course'],
        'language': request.form['language'],
        'comment': request.form['comment'],
        'checkbox': request.form['checkbox']
    }
    Survey.add_survey(data)

    return redirect('/results')