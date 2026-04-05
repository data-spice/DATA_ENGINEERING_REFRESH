#!/usr/bin/env python
# coding: utf-8

# In[47]:

year=2021
month=1
from sqlalchemy import create_engine
import pandas as pd
from tqdm.auto import tqdm

# In[48]:


prefix ='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow'
url=f'{prefix}/yellow_tripdata_{year}-{month}.csv.gz'


# In[49]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

pg_user= 'root'
pg_pass='root'
pg_host='localhost'
pg_port=5433
pg_db='my_taxi'

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[50]:


df.head()


# In[51]:


len(df)


# In[52]:


df.tail()


# In[53]:



engine=create_engine('postgresql://root:root@localhost:5433/my_taxi')


# In[54]:


df.head(0)


# In[55]:


df.head(0).to_sql(name="yellow_taxi_data",con=engine,if_exists='replace')


# In[56]:


df_iter=pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000
)


# In[57]:





# In[58]:


for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(name='yellow_taxi_data',con=engine,if_exists='append')



# In[ ]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[ ]:


len(df)


# In[ ]:

if __name__ == '__main__':
    run()


