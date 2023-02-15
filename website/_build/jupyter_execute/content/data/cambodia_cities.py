#!/usr/bin/env python
# coding: utf-8

# # Cambodia cities
# 
# ```{important}
# Please see [here](data_cam_cities) for more details
# ```

# In[1]:


import geopandas


# Original dataset is downloaded (manually) from:

# In[2]:


url = (
    "https://jeodpp.jrc.ec.europa.eu/ftp/"\
    "jrc-opendata/GHSL/GHS_STAT_UCDB2015MT_GLOBE_R2019A/"\
    "V1-2/GHS_STAT_UCDB2015MT_GLOBE_R2019A.zip/GHS_STAT_UCDB2015MT_GLOBE_R2019A_V1_2.gpkg"
)
url


# ## Read

# Then read in:

# In[3]:


p = "GHS_STAT_UCDB2015MT_GLOBE_R2019A/GHS_STAT_UCDB2015MT_GLOBE_R2019A_V1_2.gpkg"
db = geopandas.read_file(p)


# ## Thin

# We are interested in Cambodian cities only:

# In[4]:


khm = db.query("CTR_MN_NM == 'Cambodia'")


# And only on a subset of the attributes available:

# In[5]:


vars_to_keep = [
    "ID_HDC_G0", # Unique ID
    "UC_NM_MN",  # City name
    "NTL_AV",    # Mean night time light
    "E_GR_AV14", # Mean greenness 2014
    "geometry"
]


# ## Centroid for geoms

# In[6]:


khm.geometry = khm.to_crs(
    epsg=5726
).centroid.to_crs(
    epsg=4326
)


# ## Write out

# In[7]:


out_f = "cambodian_cities.geojson"
get_ipython().system(' rm -f $out_f')
khm[vars_to_keep].to_file(out_f, driver="GeoJSON")
get_ipython().system(' du -h $out_f')

