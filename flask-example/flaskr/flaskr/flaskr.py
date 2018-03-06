import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash,current_app

#create the app instane

app = Flask(__name__)
#load config from this file
app.config.from_object(__name__)

#override the default config setting from an env variable
app.config.update(dict(
    DATABASE = os.path.join(app.root_path,'flaskr.db'),
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default',
))
app.config.from_envvar('FLASKR_SETTINGS',silent=True)



def connect_db():
    rv = sqlite3.connect(current_app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    database = get_db()
    with current_app.open_resource('schema.sql',mode='r') as f:
        database.cursor().executescript(f.read())
    database.commit()


def get_db():
    '''open a new db connection if there is none yet for the current app context'''
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    '''close the db again at the end of the request'''
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()


@app.cli.command('initdb')
def initdb_command():
    ''' Init the database'''
    init_db()
    print("Database initialized")


@app.route("/")
def show_entries():
    db = get_db()
    cursor = db.execute('select title, text from entries order by id desc')
    entries = cursor.fetchall()
    return render_template('show_entries.html',entries=entries)


@app.route('/add',method=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries(title,text) values (?,?)',[request.form['title'],request.form['text']])
    db.commit()
    flash('New entry was successfully posted!')
    return redirect(url_for('show_entries'))


@app.route("/login",method=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were fooked logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html',error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('logged out now, bitch!')
    return redirect(url_for('show_entries'))
