#!/usr/bin/env python
# coding: utf-8

# # Spatial Networks

# ## 📖 Ahead of time...

# ```{margin}
# Thank you very much to [Martin Fleischmann](https://martinfleischmann.net/) for providing support and ideas in the development of this block
# ```
# 
# In this block we cover some of the analytics you can obtain when you consider street networks as spatial graphs rather than as geo-tables. 
# 
# - A good example of applying concepts and ideas presented in this block is Boeing (2020) {cite}`boeing2020off`
# - Boeing (2017) {cite}`boeing_osmnx_2017` provides a general overview on the `osmnx` project
# - A brief overview of `momepy`, the package for urban morphometrics, available in Fleischmann (2019) {cite}`fleischmann2019momepy`

# ## 💻 Hands-on coding

# In[1]:


import pandas
import geopandas
import momepy
import networkx as nx
import contextily
import matplotlib.pyplot as plt


# ````{tabbed} Local files
# 
# Assuming you have the file locally on the path `../data/`: 
# 
# ```python
# db = geopandas.read_file("../data/arturo_streets.gpkg")
# ```
# ````
# 
# ````{tabbed} Online read
# 
# If you're online, you can do:
# 
# ```python
# db = geopandas.read_file(
#     "http://darribas.org/gds4ae/_downloads/67d5480f98453027d59bf49606a7ad92/arturo_streets.gpkg"
# )
# ```
# ````
# 

# In[2]:


db = geopandas.read_file("../data/arturo_streets.gpkg")


# To make things easier later, we "explode" the table so it is made up of `LINESTRINGS` instead of `MULTILINESTRINGS`:

# In[3]:


db_tab = db.explode().reset_index()


# In[4]:


ax = db_tab.plot(
    linewidth=0.05, color="k", figsize=(4, 4)
)
ax.set_axis_off();


# In[5]:


db_tab.head()


# ### Analysing street geo-tables

# #### Length

# In[6]:


length = db_tab.to_crs(
    epsg=32630 # Expressed in metres
).geometry.length
length.head()


# In[7]:


ax = db_tab.assign(
    length=length
).plot(
    "length", 
    scheme="fisherjenkssampled", 
    k=9, 
    legend=True, 
    linewidth=0.5,
    figsize=(12, 12),
    cmap="magma"
)
contextily.add_basemap(
    ax, 
    crs=db_tab.crs, 
    source=contextily.providers.CartoDB.PositronNoLabels,
    alpha=0.5
)
ax.set_title("Street segment length");


# ````{admonition} Challenge
# Create a quantile choropleth of length for the section of the network with `dist_barri` values starting by `01`.
# 
# Bonus tip: you can create the subset of the network using the `isin` method:
# 
# ```%python
# ids = ['0101', '0102', '0103', '0104', '0105', '0106']
# subnet = db_tab[db_tab['dist_barri'].isin(ids)]
# ```
# ````

# #### Linearity

# In[8]:


linearity = momepy.Linearity(db_tab).series
linearity.head()


# In[9]:


ax = db_tab.assign(
    linearity=linearity
).plot(
    "linearity", 
    scheme="fisherjenkssampled", 
    k=9, 
    legend=True, 
    linewidth=0.5,
    figsize=(12, 12),
    cmap="magma"
)
contextily.add_basemap(
    ax, 
    crs=db_tab.crs, 
    source=contextily.providers.CartoDB.PositronNoLabels,
    alpha=0.5
)
ax.set_title("Street segment linearity");


# ```{admonition} Challenge
# Create a choropleth of linearity for the `subnet` table you have created above
# ```

# ### Streets as spatial graphs

# From geo-table to spatial graph:

# In[10]:


db_graph = momepy.gdf_to_nx(db_tab)

db_graph


# Now `db_graph` is a different animal than `db` that emphasizes *connections* rather than attributes.

# In[11]:


db_graph.is_directed()


# In[12]:


db_graph.is_multigraph()


# The (first and last) coordinates of each street segment become the ID for each segment in the graph:

# In[13]:


print(db_tab.loc[0, "geometry"])


# In[14]:


l = db_tab.loc[0, "geometry"]
l.coords


# In[15]:


node0a, node0b = edge0 = list(
    db_tab.loc[0, "geometry"].coords
)
edge0


# We can use those to extract adjacencies to each node:

# In[16]:


db_graph[node0a]


# We can access edge information for each pair of nodes with a concatenated dict query:

# In[17]:


db_graph[node0a][node0b]


# In[18]:


db_graph[node0a][node0b][0]


# In[19]:


db_graph[node0a][node0b][0]["geometry"]


# If we need all the node IDs:

# In[20]:


list(
    db_graph.nodes
)[:5] # Limit to the first five elements


# And same for edges:
# 
# ````{margin}
# ```{note}
# `edges` returns a triplet with the origin and destination node IDs, *and* the ID of the edge, which is linked to the ID of the segment in the geo-table
# ```
# ````

# In[21]:


list(
    db_graph.edges
)[:5] # Limit to the first five elements


# Or:

# In[22]:


db_graph.edges[node0a, node0b, 0]


# If you want fast access to adjacencies:

# In[23]:


db_graph.adj[node0a]


# ```{admonition} Challenge
# Create the graph version of `subnet` and consider the street segment indexed in the table as `53271`. Check the adjacencies on both ends of the segment using `db_graph` and `subnet`. *Are they the same in both graphs? Why?*
# ```

# ### Analysing graphs

# There are _many_ ways to extract information and descriptives from a graph. In this section we will explore a few that can tell us important information about the position of a node or edge in the network and about the broader characteristics of sections of the graph.

# #### Degree

# Degree tells us the number of neighbors of every edge, that is how many other nodes it is directly connected to.

# In[24]:


degree = list(db_graph.degree)
degree[:5]


# #### Node centrality

# Fraction of nodes a node is connected to:

# In[25]:


nc = pandas.Series(
    nx.degree_centrality(db_graph)
)
nc.head()


# In[26]:


nc.plot.hist(bins=100, figsize=(6, 3));


# ```{tip}
# Other variations of centrality measures are available in `networkx`. The are computationally demanding but relatively straightforward to calculate using the library. For a few of those, you can check:
# 
# - [This `networkx` example](https://networkx.org/documentation/stable/auto_examples/algorithms/plot_krackhardt_centrality.html#sphx-glr-auto-examples-algorithms-plot-krackhardt-centrality-py)
# - [The `momepy` documentation on centrality](http://docs.momepy.org/en/stable/user_guide/graph/centrality.html#Closeness-centrality)
# ```

# ```{admonition} Challenge
# Create a histogram of degree for `db_graph`. Now replicate the figure for the case of `subnet`. *What can you learn about the two graphs by doing this exercise?*
# ```

# #### Meshedness

# The [messedness](http://docs.momepy.org/en/stable/generated/momepy.meshedness.html#momepy.meshedness) of a graph captures the degree of node edge density as compared to that of nodes. Higher meshedness is related to denser, more inter-connected grids.

# In[27]:


get_ipython().run_line_magic('time', 'meshd = momepy.meshedness(db_graph, distance=500)')


# In[28]:


meshd.nodes[node0a]


# In[29]:


pandas.Series(
    {i: meshd.nodes[i]["meshedness"] for i in meshd.nodes}
).plot.hist(bins=100, figsize=(9, 4));


# ```{admonition} Challenge
# Replicate the computation of meshedness for `sub_graph` using a threshold of 250m and 500m. How do the distributions of both compare with each other?
# ```

# #### Betweenness centrality
# 
# *How often do shortest-path routes pass through a given node?*
# 
# This is computationally very demanding, so we will work on a subset of the full graph:

# In[30]:


ids = ['0101', '0102', '0103', '0104', '0105', '0106']
subnet = db_tab[db_tab['dist_barri'].isin(ids)]
sub_graph = momepy.gdf_to_nx(subnet)
node_sub = subnet.loc[53271, 'geometry'].coords[0]


# Calculating it is trivial with `momepy`:

# In[31]:


get_ipython().run_cell_magic('time', '', 'betweenness = momepy.betweenness_centrality(sub_graph)\n')


# As with meshedness, we obtain another graph in return with the information attached to it:

# In[32]:


betweenness.nodes[node_sub]


# ### Attaching information to street segments
# 
# 

# The trick here is to be able to transfer back the information stored as graphs into geo-tables so we can apply everything we already now about manipulating and mapping data in that structure. With `momepy`, we can bring a graph back into a geo-table:

# In[33]:


nodes = momepy.nx_to_gdf(
    meshd, points=True, lines=False
)


# In[34]:


nodes.head()


# In[35]:


ax = nodes.plot(
    "meshedness", 
    scheme="fisherjenkssampled",
    markersize=0.1,
    legend=True, 
    figsize=(12, 12)
)
contextily.add_basemap(
    ax, 
    crs=nodes.crs,
    source=contextily.providers.CartoDB.DarkMatterNoLabels
)
ax.set_title("Meshedness");


# With other measures index on node IDs, we can use joining machinery in `pandas`:

# In[36]:


nc.head()


# In[37]:


degree_tab = pandas.DataFrame(
    degree, columns=["id", "degree"]
)
degree_tab.index = pandas.MultiIndex.from_tuples(
    degree_tab["id"]
)
degree_tab = degree_tab["degree"]
degree_tab.head()


# In[38]:


net_stats = pandas.DataFrame(
    {"degree": degree_tab, "centrality": nc},
)
net_stats.index.names = ["x", "y"]
net_stats.head()


# In[39]:


net_stats_geo = nodes.assign(
    x=nodes.geometry.x
).assign(
    y=nodes.geometry.y
).set_index(
    ["x", "y"]
).join(net_stats)

net_stats_geo.head()


# In[40]:


f, axs = plt.subplots(1, 2, figsize=(18, 9))
vars_to_plot = ["degree", "centrality"]
for i in range(2):
    net_stats_geo.plot(
        vars_to_plot[i], 
        scheme="fisherjenkssampled",
        markersize=0.2,
        legend=True, 
        ax=axs[i]
    )
    contextily.add_basemap(
        axs[i], 
        crs=nodes.crs,
        source=contextily.providers.CartoDB.DarkMatterNoLabels
    )
    axs[i].set_title(f"Node {vars_to_plot[i]}")


# ```{admonition} Challenge
# Create choropleths for node and betweenness centrality for `sub_graph`. *How do they compare?*
# ```

# ## 🐾 Next steps

# If you found the content in this block useful, the following resources represent some suggestions on where to go next:
# 
# - The [NetworkX tutorial](https://networkx.org/documentation/stable/tutorial.html) is a great place to get a better grasp of the data structures we use to represent (spatial) graphs
# - Parts of the block benefit from the section on [urban networks](https://github.com/gboeing/ppd599/blob/master/modules/07-urban-networks-i/lecture.ipynb) in Geoff Boeing's excellent [course on Urban Data Science](https://github.com/gboeing/ppd599)
# - If you are interested in urban morphometric analysis (the study of the shape of different elements making up cities), the [`momepy`](http://docs.momepy.org/en/stable/) library is an excellent reference to absorb, including its [user guide](http://docs.momepy.org/en/stable/user_guide/intro.html)
# 
