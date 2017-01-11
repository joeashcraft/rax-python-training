#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_flask` -- serving up REST
=========================================

LAB_FLASK Learning Objective: Learn to serve RESTful APIs using the Flask library
::

 a. Using Flask create a simple server that serves the following string for the root route ('/'):
  "<h1>Welcome to my server</h1>"

 b. Add a route for "/now" that returns the current date and time in string format.

 c. Add a route that converts Fahrenheit to Centigrade and accepts the value to convert
    in the url.  For instance, /fahrenheit/32.0 should return "0.0"

 d. Add a route that converts Centigrade to Fahrenheit and accepts the value to convert
    in the url.  For instance, /centigrade/0.0 should return "32.0"

"""
import time
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Welcome to my server</h1>'


@app.route('/now')
def now():
    return time.asctime()


@app.route('/centigrade/<int:centigrade>')
@app.route('/centigrade/<float:centigrade>')
def c_to_f(centigrade):
    return '{0:.2f} °F'.format(((9 / 5 * centigrade) + 32))


@app.route('/fahrenheit/<int:fahrenheit>')
@app.route('/fahrenheit/<float:fahrenheit>')
def f_to_c(fahrenheit):
    return '{0:.2f} °C'.format((5 / 9 * (fahrenheit - 32)))


if __name__ == '__main__':
    app.run(debug=True)
