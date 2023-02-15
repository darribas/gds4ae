# Overview

This resource provides an introduction to Geographic Data Science for applied economists using Python. It has been designed to be delivered within 15 hours of teaching, split into ten sessions of 1.5h each.

## How to follow along

[`GDS4AE`](home) is best followed if you can interactively tinker with its content. To do that, you will need two things:

1. A computer set up with the Jupyter Lab environment and all the required libraries (please see the {ref}`Software stack <software_stack>` part in the [Infrastructure](infrastructure) section for instructions)
1. A local copy of the materials that you can run on your own computer (see the {ref}`repository <github_repo>` section in the [Infrastructure](infrastructure) section for instructions)

Blocks have different components:

- 📖 *Ahead of time...*: materials to go on your own ahead of the live session
- 💻 *Hands-on coding*: content for the live session
- 🐾 *Next steps*: a few pointers to continue your journey on the area the block covers

## Content

The structure of content is divided in nine blocks:

- [*Introduction*](../notebooks/01-Introduction): get familiar with the computational envirionment of modern data science
- [*Spatial Data*](../notebooks/02-Spatial_data): what do spatial data look like in Python?
- [*Geovisualisation*](../notebooks/03-Geovisualisation): make (good) data maps
- *Spatial Feature Engineering* ([Part I](../notebooks/04-Spatial_feature_eng_i) and [Part II](../notebooks/05-Spatial_feature_eng_ii)): augment and massage your data using Geography before you feed them into your model
- [*OpenStreetMap*](../notebooks/06-OpenStreetMap): acquire data from the largest geo-table in the world
- [*Spatial Networks*](../notebooks/07-Spatial_networks): understand and work with spatial graphs
- [*Transport Costs*](../notebooks/08-Transport_costs): "getting there" doesn't always cost the same

Each block has its own section and is designed to be delivered in 1.5 hours approximately. The content of some of these blocks relies on external resources, all of them freely available. When that is the case, enough detail is provided in the  to understand how additional material fits in.

## *Why Python?*

There are several reasons why we have made this choice. Many of them are summarised nicely in [this article by The Economist](https://www.economist.com/science-and-technology/2018/07/19/python-has-brought-computer-programming-to-a-vast-new-audience) (paywalled).:w


```{margin}
Source: [XKCD](https://xkcd.com/353/)
```
```{image} https://imgs.xkcd.com/comics/python.png
:alt: Python
:class: bg-primary mb-1
:width: 400px
:align: center
```

## Data

All the datasets used in this resource is freely available. Some of them have been developed in the context of the resource, others are borrowed from other resources. A full list of the datasets used, together with links to the original source, or to reproducible code to generate the data used is available in the [Datasets](../data/datasets) page.

## License

The materials in this course are published under a [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license. This grants you the right to use them freely and (re-)distribute them so long as you give credit to the original creators (see the [Home page](home) for a suggested citation) and license derivative work under the same license.
