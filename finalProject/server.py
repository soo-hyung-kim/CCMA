import os
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import sqlite3

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__)

#CockroachDB Connection String to Cluster:
# databaseurl = {}

#db = SQLAlchemy()
#def create_app():
  #app = Flask(__name__, static_url_path="", static_folder="static")
  
 # db.init_app(app)
  
  #with app.app_context():
    #from mainroutes import routes
    #app.register_blueprint(routes)
    
  #db.create_all()
  
  #return app


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/volunteer')
def vol():
  return render_template('volunteer.html')

@app.route('/postrequest')
def postreq():
  for val in request.args.values(): 
    print(val)
  return render_template('success.html')

@app.route('/requests')
def req():
  return render_template('requests.html')
#def requestPage():
  #fd = open('requests.sql', 'r')
  #sqlFile = fd.read()
  #fd.close()
  
#  con = sqlite3.connect("req.db")
  #cur = con.cursor()
  #cur.execute("""INSERT INTO reqs (
  #PhoneNum varchar(255),
  #Dorm varchar(255),
  #Mask boolean,
  #Food boolean,
  #RapidTest boolean)""")
  #cur.execute("""VALUES ('2014466201', 'Freeman', False, False, True)""")
  #df = cur.execute("SELECT * FROM reqs;")
  
  #data = df.to_html()
  
  #print(df)
  
  #print(data)

  #return render_template('requests.html', data=data)

if __name__ == '__main__':
  app.run(debug=True)