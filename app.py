from flask import Flask
from flask import render_template
app = Flask(__name__)
 
@app.route('/convert/')
@app.route('/convert/<base>/<to>/<amount>')
def convert(base=None, to=None, amount=None):
  return render_template('index.html', base=base, to=to, value = value)