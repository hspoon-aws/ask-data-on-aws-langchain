#!/usr/bin/env python
# coding: utf-8

# In[2]:


import awswrangler as wr
import pandas as pd


# In[19]:


import sqlalchemy

con = sqlalchemy.create_engine('sqlite:///Chinook.db')


# In[9]:


for index, t in tables.iterrows():
    print(t['name'])
    df = pd.read_sql_query(sql, con)


# In[22]:


# Read SQL table       
pd.read_sql_query('select * from Album', con, )


# In[30]:


s3_bucket = 'hspoon-us-east-1-genai-data'
database='chinook'
table_name = 'Album'


# In[36]:


def insert_athena_table(database, table_name, con):
    
    df = pd.read_sql_table(table_name, con)
    
    # create database on data lake
    if database not in wr.catalog.databases().values:
        wr.catalog.create_database(database)

    # Storing data on Data Lake
    wr.s3.to_parquet(
        df=df,
        path=f"s3://{s3_bucket}/{database}/{table_name}",
        dataset=True,
        database=database,
        table=table_name
    )


# In[39]:


for index, t in tables.iterrows():
    table_name = t['name']
    print(database, table_name, con)
    
    insert_athena_table(database, table_name, con)
    


# In[ ]:




