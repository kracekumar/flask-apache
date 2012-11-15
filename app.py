#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from flask import Flask, session

app = Flask(__name__)
app.secret_key = "Really secret"


@app.route("/")
def index():
    try:
        print session['username']
        if 'username' in session:
            return "username: %s" %(session['username'])
        else:
            return "No username"
    except KeyError:
        session['username'] = u'flask'
        return """Username is not present in session, so we have set as `flask`"""


app.run('0.0.0.0', 3333, debug=True)
