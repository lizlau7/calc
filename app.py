import flask
from flask import Flask,request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def estimate():
   return flask.render_template('estimate.html')

@app.route('/templates/about')
def about():
   return flask.render_template('About.html')

@app.route('/templates/Estimate.html')
def about():
   return flask.render_template('estimate.html')

@app.route('/templates/Home')
def about():
   return flask.render_template('Home.html')

@app.route('/templates/index')
def about():
   return flask.render_template('index.html')


def get_values():
   value1 = flask.request.args.get('val1')
   value2 = flask.request.args.get('val2')
 

  