# Datasets

This section covers the datasets required to run the course interactively. For archival reasons, all of those listed here have been mirrored in the repository for this course so, if you have {ref}`downloaded the course <github_repo>`, you already have a local copy of them.

## Madrid

(data_abb)=
### Airbnb properties

```{admonition} Source
This dataset has been sourced from the course ["Spatial Modelling for Data Scientists"](https://gdsl-ul.github.io/san/). The file imported here corresponds to the [`v0.1.0`](https://github.com/GDSL-UL/san/releases/tag/v0.1.0) version.
```

This dataset contains a pre-processed set of properties advertised on the AirBnb website within the region of Madrid (Spain), together with house characteristics. 

- 🗃️ Data file [`madrid_abb.gpkg`](https://github.com/GDSL-UL/san/raw/v0.1.0/data/assignment_1_madrid/madrid_abb.gpkg)
- 🤖 Code used to generate the file [`[URL]`](https://github.com/GDSL-UL/san/blob/v0.1.0/data/assignment_1_madrid/clean_data.ipynb)
- ℹ️ Furhter information [`[URL]`](https://github.com/GDSL-UL/san/blob/v0.1.0/docs/11-datasets.md#madrid-airbnb)

<a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/"><img alt="License" style="border-width:0" src="https://licensebuttons.net/l/zero/1.0/88x31.png" /></a><br />This dataset is licensed under a <a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0 Universal Public Domain Dedication</a>.

(data_abb_neis)=
### Airbnb neighbourhoods

```{admonition} Source
This dataset has been directly sourced from the website [Inside Airbnb](http://insideairbnb.com). The file was imported on February 10th 2021.
```

This dataset contains neighbourhood boundaries for the city of Madrid, as provided by Inside Airbnb.

- 🗃️ Data file {download}`neighbourhoods.geojson`
- ℹ️ Furhter information [`[URL]`](http://insideairbnb.com/madrid/)

<a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/"><img alt="License" style="border-width:0" src="https://licensebuttons.net/l/zero/1.0/88x31.png" /></a><br />This dataset is licensed under a <a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0 Universal Public Domain Dedication</a>.

(data_arturo)=
### Arturo

This dataset contains the street layout of Madrid as well as scores of habitability, where available, associated with street segments. The data originate from the [Arturo Project](http://arturo.300000kms.net), by [300,000Km/s](https://300000kms.net), and the available file here is a slimmed down version of their official [street layout](http://arturo.300000kms.net/#10) distributed by the project.

- 🗃️ Data file {download}`arturo_streets.gpkg`
- 🤖 Code used to generate the file [`[Page]`](arturo_streets_prep)
- ℹ️ Furhter information [`[URL]`](https://arturo.300000kms.net)

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This dataset is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

(data_s2_120)=
### Sentinel 2 - 120m mosaic

This dataset contains four scenes for the region of Madrid (Spain) extracted from the [Digital Twin Sandbox Sentinel-2 collection](https://medium.com/sentinel-hub/digital-twin-sandbox-sentinel-2-collection-available-to-everyone-20f3b5de846e), by the SentinelHub. Each scene corresponds to the following dates in 2019:

- January 1st
- April 1st
- July 10th
- November 17th

Each scene includes red, green, blue and near-infrared bands.

- 🗃️ Data files ({download}`Jan 1st <madrid_scene_s2_120_2019-1-1.tif>`, {download}`Apr 1st <madrid_scene_s2_120_2019-4-1.tif>`, {download}`Jul 10th <madrid_scene_s2_120_2019-7-10.tif>`, {download}`Nov 27th <madrid_scene_s2_120_2019-11-27.tif>`)
- 🤖 Code used to generate the file [`[Page]`](madrid_s2)
- ℹ️ Furhter information [`[URL]`](https://github.com/sentinel-hub/public-collections/tree/main/collections/sentinel-s2-l2a-mosaic-120)

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This dataset is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

(data_s2_10)=
### Sentinel 2 - 10m GHS composite

This dataset contains a scene for the region of Madrid (Spain) extracted from the [GHS Composite S2](https://ghsl.jrc.ec.europa.eu/ghs_s2composite.php), by the European Commission.

- 🗃️ Data file {download}`madrid_scene_s2_10_tc.tif`
- 🤖 Code used to generate the file [`[Page]`](madrid_s2)
- ℹ️ Furhter information [`[URL]`](https://ghsl.jrc.ec.europa.eu/ghs_s2composite.php)

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This dataset is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

## Cambodia

(data_cam_s5)=
### Pollution

Surface with $NO_2$ measurements (tropospheric column) information attached from Sentinel 5.

- 🗃️ Data file {download}`cambodia_s5_no2.tif`
- 🤖 Code used to generate the file [`[Page]`](cambodia_pollution)
- ℹ️ Furhter information [`[URL]`](https://github.com/Sentinel-5P/data-on-s3)

(data_cam_friction)=
### Friction surfaces

This dataset is an extraction of the following two data products by Weiss et al. (2020) {cite}`weiss2020global` and distributed through the [Malaria Atlas Project](https://malariaatlas.org/explorer/#/):

- Global friction surface enumerating land-based travel walking-only speed without access to motorized transport for a nominal year 2019 (Minutes required to travel one metre)
- Global friction surface enumerating land-based travel speed with access to motorized transport for a nominal year 2019 (Minutes required to travel one metre)

Each is provided on a separate file.

- 🗃️ Data files ({download}`Motorized <cambodia_2020_motorized_friction_surface.tif>` and {download}`Walking <cambodia_2020_walking_friction_surface.tif>`)
- 🤖 Code used to generate the file [`[Page]`](cambodia_road_friction)
- ℹ️ Furhter information [`[URL]`](https://malariaatlas.org)

(data_cam_friction_reg)=
### Regional aggregates

```{admonition} Source
This dataset relies on boundaries from the [Humanitarian Data Exchange](https://data.humdata.org/). [The file](https://data.humdata.org/dataset/wfp-geonode-cambodia-admin-boundaries-level-2-districts?force_layout=desktop) is provided by the World Food Programme through the Humanitarian Data Exchange and was accessed on February 15th 2021.
```

{ref}`Pollution <data_cam_s5>` and {ref}`friction <data_cam_friction>` aggregated at Level 2 (municipality) administrative boundaries for Cambodia.

- 🗃️ Data file {download}`cambodia_regional.gpkg`
- 🤖 Code used to generate the file [`[Page]`](cambodia_regional)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This dataset is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

(data_cam_cities)=
### Cambodian cities

Extract from the Urban Centre Database (UCDB), version 1.2, of the centroid for Cambodian cities.

- 🗃️ Data file {download}`cambodian_cities.geojson`
- 🤖 Code used to generate the file [`[Page]`](cambodia_cities)
- ℹ️ Furhter information [`[URL]`](https://ghsl.jrc.ec.europa.eu/ucdb2018visual.php)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This dataset is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
