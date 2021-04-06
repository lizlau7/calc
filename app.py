import flask
from flask import Flask,request, render_template
app = Flask(__name__)

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
   return flask.render_template('estimate.html')

@app.route('/')
def index():
   return flask.render_template('index.html')

@app.route('/about')
def about():
   return flask.render_template('about.html')


def get_values():
   value1 = flask.request.args.get('val1')
   value2 = flask.request.args.get('val2')
 

  