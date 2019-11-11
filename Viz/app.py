from flask import Flask,render_template,request,json,g
from sklearn.externals.joblib import dump, load
import numpy as np
import pandas as pd
import sqlite3
import os
#filter script
import filter_collision_data as toggle


#CODE NOT COMPLETE, NOT WORKING
app = Flask(__name__)
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

#__file__ refers to current module
ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, 'data')


#change database name
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("collision")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#load html file
@app.route("/")
def index():
    cur = get_db().cursor()
    res = cur.execute("select * from collision")
    return render_template("index.html", users=res)


#NEED TO KNOW HOW FLASK CONNECT WITH SQLITE3
@app.route('/multi_query', methods=['POST'])

def multi_query():
    '''request function get selected category from front end users'
    selection and save it as a string into day variable, it then 
    gets into a sql query. 
    Likewise, all other variables are feed into the sql query 
    to produce desired csv.
    csv is then output to current path to be used by html file to
    show collision data detail'''
    db = get_db()
    
    day =  request.form['day']
    weather = request.form['weather']
    a = [day, weather]
    query = toggle.multiple_filter(a)
    filtered_df = pd.read_sql_query(query, db)

    try:
        csv_path = os.path.join(DATA, 'output.csv')
        print("csv_path - ",csv_path)
        filtered_df.to_csv(csv_path,index=False)
        
        json_obj = json.dumps({'status':'OK','csv_path':csv_path,'result':filtered_df.to_json(orient='records')})
    
        return json_obj
        
    except (RuntimeError, TypeError, NameError) as e:
        print("Error occured : ",str(e))
        return json.dumps({'status':'BAD','result':{}});


if __name__ == "__main__":
    app.run()