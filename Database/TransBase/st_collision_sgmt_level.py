#!/usr/bin/env python
# coding: utf-8

# ### This notebook shapes collision data to street segment level and compute all model features needed to the same level.

# 1. Set-up

# In[27]:


import pandas as pd
import numpy as np
from pandas import read_sql
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# 2. load data 

# In[25]:


# main table with case-level collision record
df = pd.read_csv('transbase_collision.csv')

# mapping table with traffic volume for each street segment
df_2 = pd.read_csv('st_sgmt_trnsprtn.csv')


# In[4]:


# preview main table

df.head()


# In[5]:


# preview main table

df.describe()


# In[31]:


# select the cols we need

df_select = df[['case_id_pkey','cnn_sgmt_fkey', 'collision_severity', 'pcf_viol_category', 'road_cond_1']]


# In[32]:


# preview selected cols

df_select.head()


# 3. Transform columns before aggregation
#     - step 1: frequency count of all the categorical variables needed
#     - step 2: convert categorical vars into numeric ones so that they can be agged down the line to segment level

# In[ ]:


# 3.1 collision_severity


# In[21]:


df_select['collision_severity'].value_counts()


# In[ ]:


# mapping rule

# Injury (Other Visible)        4
# Injury (Complaint of Pain)    3
# Injury (Severe)               2 
# Fatal                         1


# In[34]:


# convert!

df_select['cs_injury_4'] = np.where(df_select['collision_severity'] == 'Injury (Other Visible)', 1, 0)
df_select['cs_injury_3'] = np.where(df_select['collision_severity'] == 'Injury (Complaint of Pain)', 1, 0)
df_select['cs_injury_2'] = np.where(df_select['collision_severity'] == 'Injury (Injury (Severe))', 1, 0)
df_select['cs_injury_1'] = np.where(df_select['collision_severity'] == 'Injury (Fatal)', 1, 0)


# In[ ]:


# 3.2 pcf_viol_category


# In[23]:


df_select['pcf_viol_category'].value_counts()


# In[ ]:


# mapping rule: if associated with road attributes then 1 else 0  

# Improper Turning                                               0
# Automobile Right of Way                                        0
# Unsafe Speed                                                   0
# Other Hazardous Violation                                      0
# Traffic Signals and Signs                                      1
# Wrong Side of Road                                             0
# Improper Passing                                               0
# Unknown                                                        0
# Unsafe Lane Change                                             0
# Not Stated                                                     0
# Other Than Driver (or Pedestrian)                              0 
# Unsafe Starting or Backing                                     0 
# Following Too Closely                                          0 
# Pedestrian Violation                                           0 
# Lights                                                         0 
# Other Improper Driving                                         0 
# Pedestrian Right of Way                                        0 
# Driving or Bicycling Under the Influence of Alcohol or Drug    0 
# Impeding Traffic                                               0 
# Brakes                                                         0  
# Other Equipment                                                0  


# In[33]:


# convert!

df_select['pcf_viol_category_is_st'] = np.where(df_select['pcf_viol_category'] == 'Traffic Signals and Signs', 1, 0)


# In[ ]:


# 3.3 road_cond_1


# In[24]:


df_select['road_cond_1'].value_counts()


# In[ ]:


# mapping rule: only assign a code number for values associated with road characteristics

# No Unusual Condition           0
# Other                          0  
# Holes, Deep Ruts               1  
# Not Stated                     0  
# Construction or Repair Zone    2  
# Loose Material on Roadway      3  
# Obstruction on Roadway         4   
# Reduced Roadway Width          5   


# In[35]:


# convert!

df_select['road_cond_new_1'] = np.where(df_select['road_cond_1'] == 'Holes, Deep Ruts', 1, 0)
df_select['road_cond_new_2'] = np.where(df_select['road_cond_1'] == 'Construction or Repair Zone', 1, 0)
df_select['road_cond_new_3'] = np.where(df_select['road_cond_1'] == 'Loose Material on Roadway', 1, 0)
df_select['road_cond_new_4'] = np.where(df_select['road_cond_1'] == 'Obstruction on Roadway', 1, 0)
df_select['road_cond_new_5'] = np.where(df_select['road_cond_1'] == 'Reduced Roadway Width', 1, 0)


# 4. Merge main table and the secondary table

# In[42]:


# preview main table (filtered version)

df_select.head()


# In[50]:


# filter secondary table with cols needed

df_2_select = df_2[['cnn_sgmt_pkey', 'daily_ride_qrt', 'daily_ride_eght', 'speed_avg_mta']]


# In[51]:


# preview filtered version
# speed_avg_mta has a lot of null values

df_2_select.describe()


# In[53]:


# merge

df_3 = df_select.merge(df_2_select, left_on = 'cnn_sgmt_fkey', right_on = 'cnn_sgmt_pkey', how = 'inner')


# In[54]:


df_3.describe()


# In[55]:


df_3.head()


# 5. group by segment key and agg all features to segment level

# In[58]:


df_sgmt = df_3.groupby('cnn_sgmt_fkey').agg({'case_id_pkey':'size',
                                   'pcf_viol_category_is_st':'sum',
                                   'cs_injury_4':'sum',
                                   'cs_injury_3':'sum',
                                   'cs_injury_2':'sum',
                                   'cs_injury_1':'sum',
                                   'road_cond_new_1':'sum',
                                   'road_cond_new_2':'sum',
                                   'road_cond_new_3':'sum',
                                   'road_cond_new_4':'sum',
                                   'road_cond_new_5':'sum',
                                   'daily_ride_qrt':'sum',
                                   'daily_ride_eght':'sum',
                                   'speed_avg_mta':'mean'                                        
                                       }).reset_index()


# In[62]:


df_sgmt.head(10)


# In[60]:


df_sgmt.describe()


# 6.  compute y

# In[65]:


# Number of collision/total_trips (measured by daily_ride_qrt)
df_sgmt['y_1'] = df_sgmt['case_id_pkey'] * 1. / df_sgmt['daily_ride_qrt']

# Number of collision/total_trips (measured by daily_ride_eght)
df_sgmt['y_2'] = df_sgmt['case_id_pkey'] * 1. / df_sgmt['daily_ride_eght']


# In[66]:


df_sgmt.head(20)


# In[67]:


df_sgmt.to_csv('df_sgmt_agg_20191106.csv', index = False)


# In[ ]:




