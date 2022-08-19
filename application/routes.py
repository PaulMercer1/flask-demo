from time import sleep
from flask import redirect, url_for, render_template, request

from application import app, db
from application.models import Games
from application.forms import BasicForm

@app.route('/')
@app.route('/<error>')
def index(error=None):
    form = BasicForm(request.form)

    history = Games.query.order_by(Games.id.desc()).limit(5).all()
    return render_template('index.html', form=form, history=history, error=error)

@app.route('/add', methods=['POST'])
def add():
    form = BasicForm(request.form)

    db.session.add(Games(name=form.name.data))
    db.session.commit()

    error = next(iter(form.name.errors), None)
    return redirect(url_for('index', error=error))

@app.route('/createdb', methods=['GET'])
def createdb():
    db.create_all()
    tries = 5
    while tries > 0:
        try:        
            db.create_all()
            tries = 0
        except Exception as ex:
            tries-= 1
            sleep(5)
    
    return redirect(url_for('index'))