from flask import (Flask, flash, g, redirect, render_template, url_for)

import forms
import models
import datetime

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'asasasas@£@I£U@I£U@£U@IUA'


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database after each request."""
    g.db.close()
    return response


@app.route('/')
@app.route('/entries')
def index():
    """The index of the site, will display all journal entries."""
    stream = models.Journal.select().order_by(
        models.Journal.date.desc())
    return render_template('index.html', stream=stream)


@app.route('/entries/new', methods=('GET', 'POST'))
def create():
    """Adds a new entry to the Journal Database"""
    form = forms.NewEntry()
    if form.validate_on_submit():
        flash("Entry successfuly submitted!")
        models.Journal.create(
            title=form.title.data.strip(),
            date=form.date.data,
            time_spent=form.time_spent.data,
            learnt=form.learnt.data,
            resources=form.resources.data
        )
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


@app.route('/entries/<int:id>')
def show(id):
    """Shows each Journal entry according to it's ID, which is then displayed via detail.html"""
    view = models.Journal.select().where(models.Journal.j_id == id)
    if view.count() == 0:
        abort(404)
    return render_template('detail.html', view=view)


@app.route('/entries/<id>/edit')
def update():
    pass


@app.route('/entries/<int:id>/delete', methods=('GET', 'POST'))
def delete(id):
    """Deletes the relevant journal entry, according to it's ID."""
    try:
        x = models.Journal.delete().where(models.Journal.j_id == id).execute()
        flash("Entry Deleted!")
        return redirect(url_for('index'))
        flash("Entry Deleted!")
    except models.DoesNotExist:
        return redirect(url_for('index'))


if __name__ == '__main__':
    models.initialise()
    try:
        models.Journal.add_entry(
            title="First Entry",
            date=datetime.datetime.now(),
            time_spent="5 Hours",
            learnt="I learnt loads!",
            resources="Treehouse was good."
        )
    except ValueError:
        print("Oh nooz!")
        app.run(debug=DEBUG, host=HOST, port=PORT)
