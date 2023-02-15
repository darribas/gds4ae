#!/usr/bin/env python
# coding: utf-8

# # Introduction

# In[3]:


from IPython.display import VimeoVideo, IFrame


# ## Geographic Data Science

# ```{note}
# This section is adapted from [Block A](https://darribas.org/gds_course/content/bA/concepts_A.html) of the GDS Course {cite}`darribas_gds_course`.
# ```
# 
# Before we learn *how* to do Geographic Data Science or even *why* you would want to do it, let's start with *what* it is. We will rely on two resources:
# 
# - First, in this video, Dani Arribas-Bel covers the building blocks at the First [Spatial Data Science Conference](https://carto.com/spatial-data-conference/2017/), organised by [CARTO](https://carto.com/)

# In[2]:


VimeoVideo("250495898", width=700)


# ````{sidebar} [URL](https://onlinelibrary.wiley.com/doi/full/10.1111/gean.12194)
# 
# ```{figure} ../figs/gds_paper.png
# :alt: GDS Paper
# :width: 200px
# :align: left
# ```
# ````
# 
# - Second, *Geographic Data Science*, by Alex Singleton and Dani Arribas-Bel {cite}`singleton2019geographic`

# ## The computational stack
# 
# One of the core learning outcomes of this course is to get familiar with the modern computational environment that is used across industry and science to "do" Data Science. In this section, we will learn about ecosystem of concepts and tools that come together to provide the building blocks of much computational work in data science these days.
# 
# ```{margin}
# Source: [The Atlantic](https://www.theatlantic.com/science/archive/2018/04/the-scientific-paper-is-obsolete/556676/)
# ```
# 
# ```{image} ../figs/atlantic.png
# :alt: The Atlantic - The Scientific Paper is Obsolete
# :class: bg-primary mb-1
# :width: 700px
# :align: center
# ```
# 
# 
# 
# 
# 
# - *Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks*, by Adam Rule et al. {cite}`rule2019ten`
# 
# ```{margin}
# [URL](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1007007)
# ```
# 
# ```{figure} ../figs/ten_rules.png
# :alt: Ten simple rules
# :width: 500px
# :align: center
# ```
# 
# 
# 
# 
# 
# - *GIS and Computational Notebooks*, by Geoff Boeing and Dani Arribas-Bel {cite}`boeing_arribasbel_2020`
# 
# ```{margin}
# [URL](https://gistbok.ucgis.org/bok-topics/gis-and-computational-notebooks)
# ```
# 
# ```{figure} ../figs/gisbok.png
# :alt: GIS and notebooks
# :width: 500px
# :align: center
# ```
# 
# 
# 
# 
# Now we are familiar with the conceptual pillars on top of which we will be working, let's switch gears into a more practical perspective. The following two clips cover the basics of Jupyter Lab, the frontend that glues all the pieces together, and Jupyter Notebooks, the file format, application, and protocol that allows us to record, store and share workflows.
# 
# ```{note}
# The clips are sourced from [Block A](https://darribas.org/gds_course/content/bA/lab_A.html) of the GDS Course {cite}`darribas_gds_course`
# ```

# ### Jupyter Lab

# In[4]:


IFrame(
    "https://liverpool.instructuremedia.com/embed/bd9e43bf-9fca-4ecb-b3b1-ce5f4990a9f0",
    width=700,
    height=300
)


# ### Jupyter Notebooks

# In[5]:


IFrame(
    "https://liverpool.instructuremedia.com/embed/6257e2a6-5af2-4fd7-9a9a-31a6818b25e2",
    width=700,
    height=300
)

