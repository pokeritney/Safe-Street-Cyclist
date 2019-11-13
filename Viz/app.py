from flask import Flask,render_template,request,g, url_for
import pandas as pd
import sqlite3
import os

DATABASE = "./collision.db"

#Create app
app = Flask(__name__)

#__file__ refers to current module
ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(ROOT, 'static')
RES = os.path.join(STATIC, 'res')

#connect to database
def get_db():
    db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    #index.html MUST be inside ./templates
    return render_template("index.html")

#filter function
def multiple_filter(user_input):
    '''input: user_input - a list of strings: user's selection
    e.g., user_input = [day, weather] and day = Wednesday, weather = Cloudy
    return: requested SQL statement
    Currently the code ONLY TEST TWO COLUMNS'''
    
    col_name = ["day_of_week", "weather_1"]
    #check if users selected anything
    var = list(set(user_input))
    
    #if not, return all collision cases
    if len(var) == 1 and var[0] == "All":
        query = "SELECT * FROM collision"
    #if yes, return selected ones
    else:
        query = 'SELECT * FROM collision WHERE '
        count = 0
        for i, c in enumerate(user_input):
            if c != "All":
                count += 1
                v = col_name[i]
                if count > 1:
                    c_filter = ' AND {} = "{}"'.format(v, c)
                    query += c_filter
                else:
                    c_filter = '{} = "{}"'.format(v, c)
                    query += c_filter
    return query


#query from user input
@app.route('/query_user', methods=['GET', 'POST'])
def query_user():
    '''Proposed logic:
    request function get selected category from users' selection 
    and save it as a string into day variable, it then 
    gets into multi_filter to produce a sql query. 
    Likewise, all other variables are feed into the sql query 
    to produce filtered csv.
    csv is then output to current path to be used by html file to
    show collision data detail'''
    
    day =  request.form['day']
    weather = request.form['weather']
    a = [day, weather]
    print(a)
    db = get_db()
    query = multiple_filter(a)
    filtered_df = pd.read_sql_query(query, db)
    
    csv_path = os.path.join(RES, 'output.csv')
    print("csv_path - ",csv_path)
    filtered_df.to_csv(csv_path,index=False)
        
    return render_template("index.html")
                
if __name__ == "__main__":
    app.run()