

@app.route('/', methods=['GET', 'POST'])
def home():
   return flask.render_template('estimate.html')

def get_values():
   value1 = flask.request.args.get('val1')
   value2 = flask.request.args.get('val2')
   value3 = (2 * 3.14 * (value2*value1)+ (3.14 *value2^2) / 144) * 25 +
        (2 * 3.14 * (value2*value1)+ (3.14 *value2^2) / 144) * 15}
   return flask.jsonify({'data':f'<p>The result is: {value3} <p>}) 
   
  