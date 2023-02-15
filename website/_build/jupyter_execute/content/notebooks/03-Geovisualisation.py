#!/usr/bin/env python
# coding: utf-8

# # Geovisualisation

# ## 📖 Ahead of time...

# This block is all about visualising statistical data on top of a geography. Although this task looks simple, there are a few technical and conceptual building blocks that it helps to understand before we try to make our own maps. Aim to complete the following readings by the time we get our hands on the keyboard: 
# 
# - [Block D](https://darribas.org/gds_course/content/bD/concepts_D.html) of the GDS course {cite}`darribas_gds_course`, which provides an introduction to choropleths (statistical maps)
# - [Chapter 5](https://geographicdata.science/book/notebooks/05_choropleth.html) of the GDS Book {cite}`reyABwolf`, discussing choropleths in more detail
# 

# ## 💻 Hands-on coding

# In[1]:


import geopandas
import xarray, rioxarray
import contextily
import seaborn as sns
from pysal.viz import mapclassify as mc
from legendgram import legendgram
import matplotlib.pyplot as plt
import palettable.matplotlib as palmpl
from splot.mapping import vba_choropleth


# ### Data

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
# db = geopandas.read_file("../data/cambodia_regional.gpkg")
# ```
# ````
# 
# ````{tabbed} Online read
# 
# If you're online, you can do:
# 
# ```python
# db = geopandas.read_file(
#     "https://darribas.org/gds4ae/_downloads/9366d230310a8a68b2ce6cf2787a2f1c/cambodia_regional.gpkg"
# )
# ```
# ````
# 

# In[2]:


db = geopandas.read_file("../data/cambodia_regional.gpkg")


# In[3]:


ax = db.to_crs(
    epsg=3857
).plot(
    edgecolor="red",
    facecolor="none",
    linewidth=2,
    alpha=0.25,
    figsize=(9, 9)
)
contextily.add_basemap(
    ax,
    source=contextily.providers.Esri.NatGeoWorldMap
)
ax.set_axis_off();


# In[4]:


db.info()


# We will use the average measurement of [nitrogen dioxide](http://www.tropomi.eu/data-products/nitrogen-dioxide) (`no2_mean`) by region throughout the block. 
# 
# To make visualisation a bit easier below, we create an additional column with values rescaled:

# In[5]:


db["no2_viz"] = db["no2_mean"] * 1e5


# This way, numbers are larger and will fit more easily on legends:

# In[6]:


db[["no2_mean", "no2_viz"]].describe()


# ### Choropleths

# In[7]:


ax = db.to_crs(
    epsg=3857
).plot(
    "no2_viz", 
    legend=True,
    figsize=(12, 9)
)
contextily.add_basemap(
    ax, 
    source=contextily.providers.CartoDB.VoyagerOnlyLabels,
    zoom=7
);


# #### A classiffication problem

# In[8]:


db["no2_viz"].unique().shape


# In[9]:


sns.displot(
    db, x="no2_viz", kde=True, aspect=2
);


# #### How to assign colors?

# ```{attention}
# To build an intuition behind each classification algorithm more easily, we create a helper method (`plot_classi`) that generates a visualisation of a given classification.
# 
# Toggle the cell below if you are interested in the code behind it.
# ```

# In[10]:


def plot_classi(classi, col, db):
    """
    Illustrate a classiffication
    ...
    
    Arguments
    ---------
    classi : mapclassify.classifiers
             Classification object
    col    : str
             Column name used for `classi`
    db     : geopandas.GeoDataFrame
             Geo-table with data for
             the classification    
    """
    f, ax = plt.subplots(figsize=(12, 6))
    ax.set_title(classi.name)
    # KDE
    sns.kdeplot(
        db[col], fill=True, ax=ax
    )
    for i in range(0, len(classi.bins)-1):
        ax.axvline(classi.bins[i], color="red")
    # Map
    aux = f.add_axes([.6, .45, .32, .4])
    db.assign(lbls=classi.yb).plot(
        "lbls", cmap="viridis", ax=aux
    )
    aux.set_axis_off()
    return None


# - Equal intervals

# In[11]:


classi = mc.EqualInterval(db["no2_viz"], k=7)
classi


# In[12]:


plot_classi(classi, "no2_viz", db)


# - Quantiles

# In[13]:


classi = mc.Quantiles(db["no2_viz"], k=7)
classi


# In[14]:


plot_classi(classi, "no2_viz", db)


# - Fisher-Jenks

# In[15]:


classi = mc.FisherJenks(db["no2_viz"], k=7)
classi


# In[16]:


plot_classi(classi, "no2_viz", db)


# ---
# 
# Now let's dig into the internals of `classi`:

# In[17]:


classi


# In[18]:


classi.k


# In[19]:


classi.bins


# In[20]:


classi.yb


# #### How *many* colors?

# ````{margin}
# ```{attention}
# The code used to generate this figure uses more advanced features than planned for this course.
# 
# If you want to inspect it, toggle the cell below.
# ```
# ````

# In[21]:


vals = [3, 5, 7, 9, 12, 15]
algos = ["equal_interval", "quantiles", "fisherjenks"]
f, axs = plt.subplots(
    len(algos), len(vals), figsize=(3*len(vals), 3*len(algos))
)
for i in range(len(algos)):
    for j in range(len(vals)):
        db.plot(
            "no2_viz", scheme=algos[i], k=vals[j], ax=axs[i, j]
        )
        axs[i, j].set_axis_off()
        if i==0:
            axs[i, j].set_title(f"k={vals[j]}")
        if j==0:
            axs[i, j].text(
                -0.1, 
                0.5, 
                algos[i], 
                horizontalalignment='center',
                verticalalignment='center', 
                transform=axs[i, j].transAxes,
                rotation=90
            )


# #### Using the *right* color

# ```{margin}
# For a safe choice, make sure to visit [ColorBrewer](https://colorbrewer2.org/)
# ```
# 
# * [<img src="../figs/l04_pal_qual.png" alt="Qualitative"
# style="width:300px;height:50px;vertical-align:middle;border:0px;" class="fragment"/>](https://jiffyclub.github.io/palettable/wesanderson/#fantasticfox2_5) **Categories**, non-ordered
# * [<img src="../figs/l04_pal_seq.png" alt="Sequential"
# style="width:300px;height:50px;vertical-align:middle;border:0px;" class="fragment"/>](https://jiffyclub.github.io/palettable/colorbrewer/sequential/#rdpu_5) Graduated, **sequential**
# * [<img src="../figs/l04_pal_div.png" alt="Divergent"
# style="width:300px;height:50px;vertical-align:middle;border:0px;" class="fragment"/>](https://jiffyclub.github.io/palettable/colorbrewer/diverging/#rdylgn_5) Graduated, **divergent**

# ### Choropleths on Geo-Tables

# #### Streamlined

# How can we create classifications from data on geo-tables? Two ways:
# 
# - Directly within `plot` (only for some algorithms)

# In[22]:


db.plot(
    "no2_viz", scheme="quantiles", k=7, legend=True
);


# ```{margin}
# See [this tutorial](https://pysal.org/mapclassify/notebooks/03_choropleth.html) for more details on fine tuning choropleths manually
# ```
# 
# ```{admonition} Challenge
# Create an equal interval map with five bins for `no2_viz`
# ```
# 
# #### Manual approach
# 
# This is valid for any algorithm and provides much more flexibility at the cost of effort.

# In[23]:


classi = mc.Quantiles(db["no2_viz"], k=7)
db.assign(
    classes=classi.yb
).plot("classes");


# #### Value by alpha mapping
# 
# ```{margin}
# See [here](https://github.com/pysal/splot/blob/main/notebooks/mapping_vba.ipynb) for more examples of VBA mapping.
# ```

# In[24]:


db['area_inv'] = 1 / db.to_crs(epsg=5726).area


# In[25]:


ax = db.plot('area_inv', scheme='quantiles')
ax.set_title('area_inv')
ax.set_axis_off();


# In[26]:


# Set up figure and axis
f, ax = plt.subplots(1, figsize=(12, 9))
# VBA choropleth
vba_choropleth(
    'no2_viz',          # Column for color 
    'area_inv',         # Column for transparency (alpha)
    db,                 # Geo-table
    rgb_mapclassify={   # Options for color classification
        'classifier': 'quantiles', 'k':5
    },
    alpha_mapclassify={ # Options for alpha classification
        'classifier': 'quantiles', 'k':5
    },
    legend=True,        # Add legend
    ax=ax               # Axis
)
# Add boundary lines
db.plot(color='none', linewidth=0.05, ax=ax);


# #### *Legendgrams*
# 
# Legendgrams are a way to more closely connect the statistical characteristics of your data to the map display.
# 
# ```{warning}
# Legendgrams are _experimental_ at the moment so the code is a bit more involved and less stable. Use at your own risk!
# ```
# 
# Unfold the cell for an example.

# In[27]:


f, ax = plt.subplots(figsize=(9, 9))

classi = mc.Quantiles(db["no2_viz"], k=7)

db.assign(
    classes=classi.yb
).plot("classes", ax=ax)

legendgram(
    f,                   # Figure object
    ax,                  # Axis object of the map
    db["no2_viz"],       # Values for the histogram
    classi.bins,         # Bin boundaries
    pal=palmpl.Viridis_7,# color palette (as palettable object)
    legend_size=(.5,.2), # legend size in fractions of the axis
    loc = 'lower right', # matplotlib-style legend locations
)
ax.set_axis_off();


# ```{admonition} Challenge
# Give [Task I](https://darribas.org/gds_course/content/bD/diy_D.html#task-i-ahah-choropleths) in [this block](https://darribas.org/gds_course/content/bD/diy_D.html) of the GDS course a go.
# ```

# ### Choropleths on surfaces

# ```{margin} Data
# If you want to read more about the data sources behind this dataset, head to the [Datasets](../data/datasets) section
# ```
# 
# 
# ````{tabbed} Local files
# 
# Assuming you have the file locally on the path `../data/`: 
# 
# ```python
# grid = xarray.open_rasterio(
#     "../data/cambodia_s5_no2.tif"
# ).sel(band=1)
# ```
# ````
# 
# ````{tabbed} Online read
# 
# If you're online, you can do:
# 
# ```python
# grid = xarray.open_rasterio(
#     "https://darribas.org/gds4ae/_downloads/0d14506cd792aecf73dd0f7f027e95b4/cambodia_s5_no2.tif"
# ).sel(band=1)
# ```
# ````
# 

# In[28]:


grid = xarray.open_rasterio("../data/cambodia_s5_no2.tif").sel(band=1)


# - (Implicit) continuous equal interval

# In[29]:


grid.where(
    grid != grid.rio.nodata
).plot(cmap="viridis");


# In[30]:


grid.where(
    grid != grid.rio.nodata
).plot(cmap="viridis", robust=True);


# - Discrete equal interval

# In[31]:


grid.where(
    grid != grid.rio.nodata
).plot(cmap="viridis", levels=7)


# - Combining with `mapclassify`

# In[32]:


grid_nona = grid.where(
    grid != grid.rio.nodata
)

classi = mc.Quantiles(
    grid_nona.to_series().dropna(), k=7
)

grid_nona.plot(
    cmap="viridis", levels=classi.bins
)
plt.title(classi.name);


# In[33]:


grid_nona = grid.where(
    grid != grid.rio.nodata
)

classi = mc.FisherJenksSampled(
    grid_nona.to_series().dropna().values, k=7
)

grid_nona.plot(
    cmap="viridis", levels=classi.bins
)
plt.title(classi.name);


# In[34]:


grid_nona = grid.where(
    grid != grid.rio.nodata
)

classi = mc.StdMean(
    grid_nona.to_series().dropna().values
)

grid_nona.plot(
    cmap="coolwarm", levels=classi.bins
)
plt.title(classi.name);


# In[35]:


grid_nona = grid.where(
    grid != grid.rio.nodata
)

classi = mc.BoxPlot(
    grid_nona.to_series().dropna().values
)

grid_nona.plot(
    cmap="coolwarm", levels=classi.bins
)
plt.title(classi.name);


# ```{admonition} Challenge
# Read the satellite image for Madrid used in the [previous section](02-Spatial_data) and create three choropleths, one for each band, using the colormaps `Reds`, `Greens`, `Blues`.
# 
# Play with different classification algorithms. 
# 
# - *Do the results change notably?*
# - *If so, why do you think that is?*
# ```

# ## 🐾 Next steps

# If you are interested in statistical maps based on classification, here are two recommendations to check out next:
# 
# - On the technical side, the [documentation for `mapclassify`](https://pysal.org/mapclassify/) (including its [tutorials](https://pysal.org/mapclassify/tutorial.html)) provides more detail and illustrates more classification algorithms than those reviewed in this block
# - On a more conceptual note, Cynthia Brewer's "Designing better maps" {cite}`brewer2015designing` is an excellent blueprint for good map making.
