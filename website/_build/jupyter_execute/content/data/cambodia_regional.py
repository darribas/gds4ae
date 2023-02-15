#!/usr/bin/env python
# coding: utf-8

# # Regional aggregates for Cambodia

# In[1]:


import pandas, geopandas
import contextily
import xarray, rioxarray
from rasterstats import zonal_stats


# ## Boundaries
# 
# ```{important}
# Please see [here](data_cam_s5) for more details
# ```

# In[2]:


url = (
    "https://geonode.wfp.org/geoserver/wfs"\
    "?format_options=charset:UTF-8&"\
    "typename=geonode:khm_adm2_un&"\
    "outputFormat=SHAPE-ZIP&"\
    "version=1.0.0&"\
    "service=WFS&"\
    "request=GetFeature"
)
url


# In[3]:


cam = geopandas.read_file(url)


# In[4]:


bb = cam.total_bounds


# ## Regional friction

# - Motorised

# In[5]:


agg_m = pandas.DataFrame(
    zonal_stats(
        cam,
        "cambodia_2020_motorized_friction_surface.tif"
    ),
    index = cam.index
)


# - Walking

# In[6]:


agg_w = pandas.DataFrame(
    zonal_stats(
        cam,
        "cambodia_2020_walking_friction_surface.tif"
    ),
    index = cam.index
)


# ## Regional pollution

# In[7]:


agg_p = pandas.DataFrame(
    zonal_stats(
        cam,
        "cambodia_s5_no2.tif",
        all_touched = True
    ),
    index = cam.index
)


# ## Join together

# In[8]:


db = cam[[
    "adm2_name", "adm2_altnm", "geometry"
]].join(
    agg_m[["mean"]].rename(columns={"mean": "motor_mean"})
).join(
    agg_w[["mean"]].rename(columns={"mean": "walk_mean"})
).join(
    agg_p[["mean"]].rename(columns={"mean": "no2_mean"})
)
db.info()


# ## Write out

# In[9]:


out_gj = "cambodia_regional.gpkg"
get_ipython().system(' rm -f $out_gj')
db.to_file(out_gj, driver="GPKG")
get_ipython().system(' du -h $out_gj')

