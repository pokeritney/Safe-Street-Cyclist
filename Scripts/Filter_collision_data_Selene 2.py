import pandas as pd
import sqlite3 as db
import os
import io

db_name = "input_databse_name"
collision = db.connect(db_name)

#For day_of_week, weather, collision_severity, primary_coll_factor, pcf_viol_category, road_cond_1
def filter_collision(col_name = "day_of_week", select = "Sunday"):
    query = 'SELECT * FROM collision WHERE' + col_name + '=' + select
    collision_filtered = pd.read_sql_query(query, collision)
    return collision_filtered

#For collision_time, NOT SURE HOW WE SHOULD PARSE THIS COLUMN
def filter_time(select = "Morning"):
    time_category = ["Morning", "Afternoon", "Sunset", "Night"]
    if select == "Morning":
        query = '''SELECT * FROM collision 
        WHERE collision_time BETWEEN 600 AND 1200'''
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