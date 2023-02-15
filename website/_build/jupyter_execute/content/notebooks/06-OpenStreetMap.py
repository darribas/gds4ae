#!/usr/bin/env python
# coding: utf-8

# # OpenStreetMap

# In[1]:


from IPython.display import YouTubeVideo


# ## 📖 Ahead of time...

# This session is all about OpenStreetMap. To provide an overview of what the project is, whether you have never heard of it or you are somewhat familiar, the followring will set your mind "on course":
# 
# - The following short clip provides a general overview of what OpenStreetMap is

# In[2]:


YouTubeVideo(
    "Phwrgb16oEM", width=700, height=300
)


# - [This recent piece](https://joemorrison.medium.com/openstreetmap-is-having-a-moment-dcc7eef1bb01) contains several interesting points about how OpenStreetMap is currently being created and some of the implications this model may have.
# - Anderson et al. (2019) {cite}`anderson2019corporate` provides some of the academic underpinnings to the views expressed in Morrison's piece

# ## 💻 Hands-on coding

# In[3]:


import geopandas
import contextily
from IPython.display import GeoJSON


# Since some of the query options we will discuss involve pre-defined extents, we will read the Madrid neighbourhoods dataset first:
# 
# 
# ````{tabbed} Local files
# 
# Assuming you have the file locally on the path `../data/`: 
# 
# ```python
# neis = geopandas.read_file("../data/neighbourhoods.geojson")
# ```
# ````
# 
# ````{tabbed} Online read
# 
# If you're online, you can do:
# 
# ```python
# neis = geopandas.read_file(
#     "http://darribas.org/gds4ae/_downloads/44b4bc22c042386c2c0f8dc6685ef17c/neighbourhoods.geojson"
# )
# ```
# ````
# 

# In[4]:


neis = geopandas.read_file("../data/neighbourhoods.geojson")


# To make some of the examples below *easy* on OpenStreetMap servers, we will single out the smallest neighborhood:

# In[5]:


areas = neis.to_crs(
    epsg=32630
).area

smallest = neis[areas == areas.min()]
smallest


# In[6]:


ax = smallest.plot(
    facecolor="none", edgecolor="blue", linewidth=2
)
contextily.add_basemap(
    ax, 
    crs=smallest.crs, 
    source=contextily.providers.OpenStreetMap.Mapnik
);


# ### `osmnx`

# In[7]:


import osmnx as ox


# ```{margin}
# Here is a trick to pin all your queries to OpenStreetMap to a specific date, so results are always reproducible, even if the map changes in the meantime.
# 
# Tip courtesy of [Martin Fleischmann](https://martinfleischmann.net/).
# ```

# In[8]:


ox.config(
    overpass_settings='[out:json][timeout:90][date:"2021-03-07T00:00:00Z"]'
)


# ```{tip}
# Much of the methods covered here rely on the `osmnx.geometries` module. Check out its reference [here](https://osmnx.readthedocs.io/en/stable/osmnx.html#module-osmnx.geometries)
# ```

# There are two broad areas to keep in mind when querying data on OpenStreetMap through `osmnx`:
# 
# - The interface to specify the *extent* of the search

# - The *nature* of the entities being queried. Here, the interface relies entirely on OpenStreetMap's tagging system. Given the distributed nature of the project, this is variable, but a good place to start is:
# 
# > [https://wiki.openstreetmap.org/wiki/Tags](https://wiki.openstreetmap.org/wiki/Tags)
# 
# 

# Generally, the interface we will follow involves the following:
# 
# ```python
# received_entities = ox.geometries_from_XXX(
#     <extent>, tags={<key>: True/<value(s)>}, ...
# )
# ```
# 
# The `<extent>` can take several forms:

# In[9]:


[i for i in dir(ox) if "geometries_from_" in i]


# The `tags` follow the [official feature spec](https://wiki.openstreetmap.org/wiki/Map_features).

# ### Buildings

# In[10]:


blgs = ox.geometries_from_polygon(
    smallest.squeeze().geometry, tags={"building": True}
)


# In[11]:


blgs.plot();


# In[12]:


blgs.info()


# In[13]:


blgs.head()


# If you want to visit the entity online, you can do so at:
# 
# > `https://www.openstreetmap.org/<unique_id>`

# ```{admonition} Challenge
# Extract the building footprints for the Sol neighbourhood in `neis`
# ```

# ### Other polygons

# In[14]:


park = ox.geometries_from_place(
    "Parque El Retiro, Madrid", tags={"leisure": "park"}
)


# In[15]:


ax = park.plot(
    facecolor="none", edgecolor="blue", linewidth=2
)
contextily.add_basemap(
    ax, 
    crs=smallest.crs, 
    source=contextily.providers.OpenStreetMap.Mapnik
);


# ### Points of interest

# Bars around Atocha station:

# In[16]:


bars = ox.geometries_from_address(
    "Puerta de Atocha, Madrid", tags={"amenity": "bar"}, dist=1500
)


# We can quickly explore with `GeoJSON`:

# ````{margin} Data
# If you have an earlier version of `geopandas` than 0.10, you can obtain a similar map with:
# 
# ```%python
# GeoJSON(bars.__geo_interface__)
# ```
# ````

# In[17]:


bars.explore()


# And stores within Malasaña:

# In[18]:


shops = ox.geometries_from_address(
    "Malasaña, Madrid, Spain", # Boundary to search within
    tags={
        "shop": True,
        "landuse": ["retail", "commercial"],
        "building": "retail"
    },
    dist=1000
)


# We use `geometries_from_place` for delineated areas ("polygonal entities"):

# In[19]:


cs = ox.geometries_from_place(
    "Madrid, Spain",
    tags={"amenity": "charging_station"}
)
cs.explore()


# Similarly, we can work with location data. For example, searches around a given point:

# In[20]:


bakeries = ox.geometries_from_point(
    (40.418881103417675, -3.6920446157455444),
    tags={"shop": "bakery", "craft": "bakery"},
    dist=500
)
GeoJSON(bakeries.__geo_interface__)


# ```{admonition} Challenge
# - *How many music shops does OSM record within 750 metres of Puerta de Alcalá?*
# - *Are there more restaurants or clothing shops within the polygon that represents the Pacífico neighbourhood in `neis` table?*
# ```

# ### Streets

# Street data can be obtained as another type of entity, as above; or as a graph object.

# #### Geo-tables

# In[21]:


centro = ox.geometries_from_polygon(
    neis.query("neighbourhood == 'Sol'").squeeze().geometry,
    tags={"highway": True}
)


# We can get a quick peak into what is returned (grey), compared to the region we used for the query:

# In[22]:


ax = neis.query(
    "neighbourhood == 'Sol'"
).plot(color="k")
centro.plot(
    ax=ax, 
    color="0.5", 
    linewidth=0.2, 
    markersize=0.5
);


# This however will return all sorts of things:

# In[23]:


centro.geometry


# #### Spatial graphs

# This returns clean, processed *graph* objects for the street network:

# In[24]:


[i for i in dir(ox) if "graph_from_" in i]


# In[25]:


centro_gr = ox.graph_from_polygon(
    neis.query("neighbourhood == 'Sol'").squeeze().geometry,
)


# ```{note}
# For more on graph representations of street networks, see [block 07](07-Spatial_networks)
# ```

# In[26]:


centro_gr


# And to visualise it:

# In[27]:


[i for i in dir(ox) if "plot_graph" in i]


# In[28]:


ox.plot_figure_ground(centro_gr);


# In[29]:


ox.plot_graph_folium(centro_gr)


# ```{admonition} Challenge
# *How many bookshops are within a 50m radious of the Paseo de la Castellana?*
# 
# Bonus tip: this one involves the following steps:
# 
# - Extracting the street segment for Paseo de la Castellana
# - Drawing a 50m buffer around it
# - Querying OSM for bookshops
# ```

# ### `pyrosm`

# If you are planning to read full collections of OpenStreetMap entities for a given region, `osmnx` might not be the ideal tool. Instead, it is possible to access extracts of regions and read them in full with [`pyrosm`](https://pyrosm.readthedocs.io/en/latest/index.html), which is faster for *these* operations.
# 
# ```{margin}
# More information about the `pyrosm` project is available on its [website](https://pyrosm.readthedocs.io/)
# ```

# In[30]:


import pyrosm


# If you are working on a "popular" place, there are utilities to acquire the data:

# In[31]:


mad = pyrosm.get_data("Madrid")
mad


# Once downloaded, we can start up the database:

# In[32]:


mad_osm = pyrosm.OSM(mad)


# And we can then read parts of all of OpenStreetMap data available for Madrid through queries to `mad_osm`. It is important to note that `pyrosm` will return queries as `GeoDataFrame` objects, but can also interoperate with graph data structures.

# ## 🐾 Next steps

# If you found the content in this block useful, the following resources represent some suggestions on where to go next:
# 
# - Parts of the block are inspired and informed by Geoff Boeing's excellent [course on Urban Data Science](https://github.com/gboeing/ppd599)
# - More in depth content about `osmnx` is available in the [official examples collection](https://github.com/gboeing/osmnx-examples)
# - Boeing (2020) {cite}`boeing2020exploring` illustrates how OpenStreetMap can be used to analyse urban form ([Open Access](https://osf.io/preprints/socarxiv/rnwgv/))
