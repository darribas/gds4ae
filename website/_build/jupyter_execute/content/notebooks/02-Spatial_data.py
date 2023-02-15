#!/usr/bin/env python
# coding: utf-8

# # Spatial Data

# ## 📖 Ahead of time...

# This block is all about understanding spatial data, both conceptually and practically. Before your fingers get on the keyboard, the following readings will help you get going and familiar with core ideas: 
# 
# - [Chapter 1](https://geographicdata.science/book/notebooks/01_geo_thinking.html) of the GDS Book {cite}`reyABwolf`, which provides a conceptual overview of representing Geography in data
# - [Chapter 3](https://geographicdata.science/book/notebooks/03_spatial_data.html) of the GDS Book {cite}`reyABwolf`, a sister chapter with a more applied perspective on how concepts are implemented in computer data structures
# 
# Additionally, parts of this block are based and source from [Block C](https://darribas.org/gds_course/content/bC/lab_C.html) in the GDS Course {cite}`darribas_gds_course`.
# 

# ## 💻 Hands-on coding

# ### (Geographic) tables

# In[1]:


import pandas
import geopandas
import xarray, rioxarray
import contextily
import matplotlib.pyplot as plt


# #### Points

# 
# ```{margin} Data
# If you want to read more about the data sources behind this dataset, head to the [Datasets](../data/datasets) section
# ```
# 
# 
# 
# ````{tabbed} Local files
# 
# Assuming you have the file locally on the path `../data/`: 
# 
# ```python
# pts = geopandas.read_file("../data/madrid_abb.gpkg")
# ```
# ````
# 
# ````{tabbed} Online read
# 
# If you're online, you can do:
# 
# ```python
# pts = geopandas.read_file(
#     "https://github.com/GDSL-UL/san/raw/v0.1.0/data/assignment_1_madrid/madrid_abb.gpkg"
# )
# ```
# ````

# In[2]:


pts = geopandas.read_file("../data/madrid_abb.gpkg")


# ````{admonition} Point geometries from columns
# :class: dropdown
# 
# Sometimes, points are provided as separate columns in an otherwise non-spatial table. For example imagine we have an object `cols` which looks like:
# 
# ```python
# cols.head()
# ```
# 
# ```
#           X         Y
# 0  0.259602  0.854351
# 1  0.661662  0.782427
# 2  0.932211  0.319130
# 3  0.395249  0.469885
# 4  0.303446  0.008525
# ```
# 
# In this case, we can convert those into proper geometries by:
# 
# ```python
# pts = geopandas.GeoSeries(
#     geopandas.points_from_xy(cols["X"], cols["Y"])
# )
# ```
# ````

# In[3]:


pts.info()


# In[4]:


pts.head()


# ```{admonition} Challenge
# Show the top ten values of of `price` and `neighbourhood`
# ```

# #### Lines

# ````{tabbed} Local files
# 
# Assuming you have the file locally on the path `../data/`: 
# 
# ```python
# pts = geopandas.read_file("../data/arturo_streets.gpkg")
# ```
# ````
# 
# ````{tabbed} Online read
# 
# If you're online, you can do:
# 
# ```python
# pts = geopandas.read_file(
#     "https://darribas.org/gds4ae/_downloads/67d5480f98453027d59bf49606a7ad92/arturo_streets.gpkg"
# )
# ```
# ````

# In[5]:


lines = geopandas.read_file("../data/arturo_streets.gpkg")


# In[6]:


lines.info()


# In[7]:


lines.loc[0, "geometry"]


# ```{admonition} Challenge
# Print descriptive statistics for `population_density` and `average_quality`
# ```

# #### Polygons

# ````{tabbed} Local files
# 
# Assuming you have the file locally on the path `../data/`: 
# 
# ```python
# polys = geopandas.read_file("../data/neighbourhoods.geojson")
# ```
# ````
# 
# ````{tabbed} Online read
# 
# If you're online, you can do:
# 
# ```python
# polys = geopandas.read_file(
#     "https://darribas.org/gds4ae/_downloads/44b4bc22c042386c2c0f8dc6685ef17c/neighbourhoods.geojson"
# )
# ```
# ````

# In[8]:


polys = geopandas.read_file("../data/neighbourhoods.geojson")


# In[9]:


polys.head()


# In[10]:


polys.query("neighbourhood_group == 'Retiro'")


# In[11]:


polys.neighbourhood_group.unique()


# ```{admonition} Challenge
# Print the neighborhoods within the "Latina" group
# ```

# ### Surfaces

# ````{tabbed} Local files
# 
# Assuming you have the file locally on the path `../data/`: 
# 
# ```python
# sat = xarray.open_rasterio("../data/madrid_scene_s2_10_tc.tif")
# ```
# ````
# 
# ````{tabbed} Online read
# 
# If you're online, you can do:
# 
# ```python
# sat = xarray.open_rasterio(
#     "https://darribas.org/gds4ae/_downloads/cafed4de0cfde63e6d2ffcb92264b431/madrid_scene_s2_10_tc.tif"
# )
# ```
# ````

# In[12]:


sat = rioxarray.open_rasterio("../data/madrid_scene_s2_10_tc.tif")


# In[13]:


sat


# In[14]:


sat.sel(band=1)


# In[15]:


sat.sel(
    x=slice(430000, 440000),  # x is ascending
    y=slice(4480000, 4470000) # y is descending
)


# ```{admonition} Challenge
# Subset `sat` to band 2 and the section within [444444, 455555] of Easting and [4470000, 4480000] of Northing. 
# 
# - *How many pixels does it contain?*
# - *What if you used bands 1 and 3 instead?*
# ```

# ### Visualisation

# ```{margin} IMPORTANT
# You will need version 0.10.0 or greater of `geopandas` to use `explore`. 
# ```

# In[16]:


polys.explore()


# In[17]:


polys.plot()


# In[18]:


ax = lines.plot(linewidth=0.1, color="black")
contextily.add_basemap(ax, crs=lines.crs)


# ```{margin}
# See more basemap options [here](https://contextily.readthedocs.io/en/latest/providers_deepdive.html).
# ```

# In[19]:


ax = pts.plot(color="red", figsize=(12, 12), markersize=0.1)
contextily.add_basemap(
    ax,
    crs = pts.crs,
    source = contextily.providers.CartoDB.DarkMatter
);


# In[20]:


sat.plot.imshow(figsize=(12, 12))


# ````{margin} IMPORTANT
# You will need version 1.1.0 of `contextily` to use label layers. Install it with:
# 
# ```shell
# pip install \
#     -U --no-deps \
#     contextily
# ```
# ````

# In[21]:


f, ax = plt.subplots(1, figsize=(12, 12))
sat.plot.imshow(ax=ax)
contextily.add_basemap(
    ax,
    crs=sat.rio.crs,
    source=contextily.providers.Stamen.TonerLabels,
    zoom=11
);


# ```{admonition} Challenge
# Make three plots of `sat`, plotting one single band in each
# ```

# ### Spatial operations

# #### (Re-)Projections

# In[22]:


pts.crs


# In[23]:


sat.rio.crs


# In[24]:


pts.to_crs(sat.rio.crs).crs


# In[25]:


sat.rio.reproject(pts.crs).rio.crs


# In[26]:


# All into Web Mercator (EPSG:3857)
f, ax = plt.subplots(1, figsize=(12, 12))
## Satellite image
sat.rio.reproject(
    "EPSG:3857"
).plot.imshow(
    ax=ax
)
## Neighbourhoods
polys.to_crs(epsg=3857).plot(
    linewidth=2, 
    edgecolor="xkcd:lime", 
    facecolor="none",
    ax=ax
)
## Labels
contextily.add_basemap( # No need to reproject
    ax,
    source=contextily.providers.Stamen.TonerLabels,
);


# #### Centroids

# ```{margin}
# Note the warning that geometric operations with non-project CRS object result in biases.
# ```

# In[27]:


polys.centroid


# In[28]:


lines.centroid


# In[29]:


ax = polys.plot(color="purple")
polys.centroid.plot(
    ax=ax, color="lime", markersize=1
)


# #### Spatial joins

# ```{margin}
# More information about spatial joins in `geopandas` is available on its [documentation page](https://geopandas.org/mergingdata.html#spatial-joins)
# ```

# In[30]:


sj = geopandas.sjoin(
    lines,
    polys.to_crs(lines.crs)
)


# In[31]:


# Subset of lines
ax = sj.query(
    "neighbourhood == 'Jerónimos'"
).plot(color="xkcd:bright turquoise")

# Subset of line centroids
ax = sj.query(
    "neighbourhood == 'Jerónimos'"
).centroid.plot(
    color="xkcd:bright violet", markersize=7, ax=ax
)

# Local basemap
contextily.add_basemap(
    ax,
    crs=sj.crs,
    source="../data/madrid_scene_s2_10_tc.tif",
    alpha=0.5
)


# In[32]:


sj.info()


# #### Areas

# In[33]:


areas = polys.to_crs(
    epsg=25830
).area * 1e-6 # Km2
areas.head()


# #### Distances

# In[34]:


cemfi = geopandas.tools.geocode(
    "Calle Casado del Alisal, 5, Madrid"
).to_crs(epsg=25830)
cemfi


# In[35]:


polys.to_crs(
    cemfi.crs
).distance(
    cemfi.geometry
)


# In[36]:


d2cemfi = polys.to_crs(
    cemfi.crs
).distance(
    cemfi.geometry[0] # NO index
)
d2cemfi.head()


# In[37]:


ax = polys.assign(
    dist=d2cemfi/1000
).plot("dist", legend=True)

cemfi.to_crs(
    polys.crs
).plot(
    marker="*", 
    markersize=15, 
    color="r", 
    label="CEMFI", 
    ax=ax
)

ax.legend()
ax.set_title(
    "Distance to CEMFI"
);


# ```{admonition} Challenge
# Give [Task III](https://darribas.org/gds_course/content/bC/diy_C.html#task-iii-the-gender-gap-on-the-streets) in this block of the GDS course a go
# ```

# ## 🐾 Next steps

# If you are interested in following up on some of the topics explored in this block, the following pointers might be useful:
# 
# - Although we have seen here `geopandas` only, all non-geographic operations on geo-tables are really thanks to `pandas`, the workhorse for tabular data in Python. Their [official documentation](https://pandas.pydata.org/docs/) is an excellent first stop. If you prefer a book, McKinney (2012) {cite}`mckinney2012python` is a great one.
# - For more detail on geographic operations on geo-tables, the [Geopandas official documentation](https://geopandas.org/) is a great place to continue the journey.
# - Surfaces, as covered here, are really an example of multi-dimensional labelled arrays. The library we use, `xarray` represents the cutting edge for working with these data structures in Python, and [their documentation](https://xarray.pydata.org/) is a great place to wrap your head around how data of this type can be manipulated. For geographic extensions (CRS handling, reprojections, etc.), we have used `rioxarray` under the hood, and [its documentation](https://corteva.github.io/rioxarray/) is also well worth checking.
