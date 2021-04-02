import flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/estimate')
def home():
   return ('estimate.html')
if __name__=='__main__':
   app.run('localhost',4999)


def get_values():
   value1 = flask.request.args.get('val1')
   value2 = flask.request.args.get('val2')
 
 @app.route('/About')
 def about():
    return flask.render_template('About.html')
