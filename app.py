import flask
from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
   return flask.render_template('estimate.html')

def get_values():
   value1 = flask.request.args.get('val1')
   value2 = flask.request.args.get('val2')
 
   
  