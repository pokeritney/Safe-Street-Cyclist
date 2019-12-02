#!/usr/bin/env python
# coding: utf-8

# ### This notebook shapes collision data to street segment level and compute all model features needed to the same level.

# 1. Set-up

# In[68]:


import pandas as pd
import numpy as np
from pandas import read_sql
import seaborn as sns
import matplotlib.pyplot as plt


# In[69]:


pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# 2. load data 

# In[106]:


# main table with case-level collision record
df = pd.read_csv('transbase_collision.csv')

# mapping table with traffic volume for each street segment
# df_2 = pd.read_csv('st_sgmt_trnsprtn.csv')

# strees_full
df_2 = pd.read_csv('streets_full.csv')


# In[71]:


# preview main table

df.head()


# In[74]:


# preview main table

df.describe()


# In[75]:


# select the cols we need

df_select = df[['case_id_pkey','cnn_sgmt_fkey', 'collision_severity']]


# In[76]:


# preview selected cols

df_select.head()


# 3. Transform variables

# In[ ]:


# 3.1 collision_severity


# In[77]:


df_select['collision_severity'].isnull().sum()


# In[21]:


df_select['collision_severity'].value_counts()


# In[78]:


# mapping rule

# Injury (Other Visible)        4
# Injury (Complaint of Pain)    3
# Injury (Severe)               2 
# Fatal                         1


# In[79]:


# convert!

df_select['cs_injury_4'] = np.where(df_select['collision_severity'] == 'Injury (Other Visible)', 1, 0)
df_select['cs_injury_3'] = np.where(df_select['collision_severity'] == 'Injury (Complaint of Pain)', 1, 0)
df_select['cs_injury_2'] = np.where(df_select['collision_severity'] == 'Injury (Injury (Severe))', 1, 0)
df_select['cs_injury_1'] = np.where(df_select['collision_severity'] == 'Injury (Fatal)', 1, 0)


# In[91]:


# roll up to segment key level

df_select_sgmt_level = df_select.groupby('cnn_sgmt_fkey').agg({'case_id_pkey':'size',
                                   'cs_injury_4':'sum',
                                   'cs_injury_3':'sum',
                                   'cs_injury_2':'sum',
                                   'cs_injury_1':'sum'                                     
                                       }).reset_index()


# In[93]:


# change colume names

df_select_sgmt_level.rename(columns={'case_id_pkey': 'num_collisions', 
                                     'cs_injury_4': 'num_cases_injury_other_visible',
                                     'cs_injury_3': 'num_cases_complaint_of_pain',
                                     'cs_injury_2': 'num_cases_severe',
                                     'cs_injury_1': 'num_cases_fatal'
                                    }, inplace=True)


# In[97]:


df_select_sgmt_level.head()


# In[98]:


# no nulls

df_select_sgmt_level.isnull().sum()


# 4. Merge df_select_sgmt_level table and the streets_full table

# In[99]:


# preview main table (filtered version)

df_select.head()


# In[107]:


df_2.head()


# In[108]:


# check nulls for each column

df_2.isnull().sum()


# In[86]:


# daily_ride_qrt has 428 nulls
# need to remove from y metric calculation because denominator cannot be null


# In[109]:


df_2_select = df_2.copy()


# In[115]:


# merge using segment key

df_3 = df_select_sgmt_level.merge(df_2, left_on = 'cnn_sgmt_fkey', right_on = 'cnn_sgmt_pkey', how = 'inner')


# In[116]:


df_3.head()


# In[117]:


df_3.isnull().sum()


# 5.  compute y

# In[119]:


# Number of collision/daily_ride_qrt

df_3_notnull = df_3[df_3['daily_ride_qrt'].isnull() == False]

df_3_notnull['y'] = df_3_notnull['num_collisions'] * 1. / df_3_notnull['daily_ride_qrt']


# In[120]:


df_3_notnull.head(20)


# In[121]:


df_3_notnull.isnull().sum()


# In[124]:


df_3_notnull['y'].describe()


# In[126]:


df_3_notnull.to_csv('model_data_segment_full_20191109.csv', index = False)


# In[ ]:




