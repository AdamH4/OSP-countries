from flask import Flask 
from flask import render_template 
import json
app = Flask(__name__, static_folder='public', static_url_path='')

countriesFile = open('static/countries.json')

data = json.load(countriesFile)

@app.route('/')
def index():
  return 'Server Greetings!'
  
@app.route('/countries')
def say_hello():
  return data

# @app.route('docs')
# def openApi():
#     return render_template('./public')

