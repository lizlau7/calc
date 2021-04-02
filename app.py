import flask
from flask import Flask,request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   return flask.render_template('estimate.html')

@app.route('/Estimate.html')
def estimate():
   return flask.render_template('Estimate.html')

def get_values():
   value1 = flask.request.args.get('val1')
   value2 = flask.request.args.get('val2')
 

  