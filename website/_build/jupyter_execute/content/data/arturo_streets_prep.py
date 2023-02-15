#!/usr/bin/env python
# coding: utf-8

# # Prepare ARTURO dataset
# 
# ```{important}
# Please see [here](data_arturo) for more details
# ```

# In[1]:


import geopandas, pandas
import momepy
from shapely import wkt


# ## Source data

# - Street layout

# In[2]:


full = geopandas.read_file(
    "http://arturo.300000kms.net/data/model.geojson.zip"
)


# - Scores

# In[3]:


scores = pandas.read_json(
    "http://www.atnight.ws/_imperdible/out/votes.json"
)


# Convert IDs to strings:

# In[4]:


scores["dm_id"] = scores["dm_id"].astype(str)


# ## Extract point locations

# - Pull out points

# In[5]:


parser = lambda s: wkt.loads(s.split(";")[1])
pts = geopandas.GeoSeries(
    full["geom_pu"].apply(parser),
    crs = "EPSG:25830"
)


# - Attach as columns

# In[6]:


full["X"] = pts.x
full["Y"] = pts.y


# ## Trim variables

# In[7]:


vars_to_keep = [
    "OGC_FID", 
    "dm_id", 
    "dist_barri", 
    "average_quality", 
    "population_density", 
    "X", 
    "Y", 
    "geometry"
]


# ## Join

# In[8]:


db = full[vars_to_keep].join(
    scores.set_index("dm_id"), on="dm_id"
).rename({"value": "arturo_score"})


# ## Write out
# 
# Note we convert to Spanish projection in metres

# In[9]:


db.to_crs(epsg=25830)\
  .to_file("arturo_streets.gpkg", driver="GPKG")

