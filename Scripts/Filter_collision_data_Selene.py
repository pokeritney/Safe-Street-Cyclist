import pandas as pd
import sqlite3 as db
import os
import io

#export_var_select > export_var_select.db
db_name = "export_var_select.db"
collision = db.connect(db_name)

#For day_of_week, weather, collision_severity, primary_coll_factor, pcf_viol_category, road_cond_1
category = ["Day of Week", "Weather", "Collision Severity", "Primary Collision Factor",
"Violation Category", "Road Condition"]

def filter_collision(col_name = "day_of_week", select = "Sunday"):
    query = 'SELECT * FROM collision WHERE' + col_name + '=' + select
    collision_filtered = pd.read_sql_query(query, collision)
    return collision_filtered

#For collision_time
time_category = ["6:00am to 8:59am", "9:00am to 11:59am", "12:00pm to 14:59pm", "15:00pm to 17:59pm", 
"18:00pm to 20:59pm", "21:00pm to 23:59pm", "00:00am to 02:59am", "03:00am to 05:59am"]

time = ["600 AND 859", "900 AND 1159", "1200 AND 1459", "1500 AND 1759",
"1800 AND 2059", "2100 AND 2359", "0 AND 259", "300 AND 559"]

def filter_time(select = "6:00am to 8:59am"):
    time_val = time[time_category.index(select)]
    query = "SELECT * FROM collision WHERE collision_time BETWEEN " +  time_val
    collision_filtered = pd.read_sql_query(query, collision)
    return collision_filtered

def query(col_name, select):
    if col_name == "collision_time":
        collision_filtered = filter_time(select)
    else:
        collision_filtered = filter_collision(col_name, select)
    return collision_filtered

def main():
    data_interested = query("day_of_week", "Sunday")
    print(data_interested)

if __name__ == '__main__':
    main()