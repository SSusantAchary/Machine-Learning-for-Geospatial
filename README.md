# **Machine Learning for Geospatial 🌍**

<p align="center">
  <img src="https://d1a3f4spazzrp4.cloudfront.net/kepler.gl/website/showcase/geojson-s.png" alt="Last-Mile Delivery Visualization" width="600">
</p>

Welcome to the **Machine Learning for Geospatial** repository! This is a curated collection of resources, tools, programming libraries, and courses dedicated to applying machine learning techniques to geospatial data. Whether you're a beginner or an experienced practitioner, this repository aims to provide everything you need to explore the fascinating intersection of machine learning and geospatial science.

---

## **Why Geospatial Machine Learning?**

Geospatial data is becoming increasingly important in solving real-world problems like urban planning, disaster management, environmental monitoring, and logistics optimization. By integrating machine learning, we can:
- Automate land cover classification from satellite imagery 🌳.
- Predict climate trends and weather anomalies 🌦️.
- Optimize routes for logistics and transportation 🚚.
- Monitor and analyze urban growth 🏙️.

---

## **📚 Resources**

### **Beginner Guides**
1. **Geospatial Data Basics**  
   - [What is GIS?](https://gisgeography.com/what-gis-geographic-information-systems/)  
   - [Understanding Raster and Vector Data](https://gisgeography.com/spatial-data-types-vector-raster/)  

2. **Intro to Machine Learning**  
   - [Machine Learning Crash Course by Google](https://developers.google.com/machine-learning/crash-course)  
   - [Kaggle’s Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)  

### **Geospatial Data Repositories**
- **Bharatmaps**: [Bharatmaps.gov.in](https://bharatmaps.gov.in/bharatmaps/)
- **ISRO-Bhuvan**: [Bhuvan-IndiaGeo-Platform of ISRO](https://bhuvan.nrsc.gov.in/ngmaps?mode=Hybrid)
- **OpenStreetMap**: [OpenStreetMap.org](https://www.openstreetmap.org/)  
- **USGS Earth Explorer**: [earthexplorer.usgs.gov](https://earthexplorer.usgs.gov/)  
- **Sentinel Hub**: [Copernicus Sentinel Data](https://scihub.copernicus.eu/)  
- **NASA Earth Science Data**: [earthdata.nasa.gov](https://earthdata.nasa.gov/)  

### **Tutorials and Articles**
- **GeoPandas Documentation**: [geopandas.org](https://geopandas.org/)  
- **Satellite Image Analysis with Python**: [Planet Univesity](https://university.planet.com/getting-started-with-analyzing-satellite-imagery-with-python/1788192/scorm/37f7ncy9a67o9)

---

## **🛠️ Tools and Programming Libraries**

### **Geospatial Libraries**
- **GeoPandas**: For handling and analyzing vector geospatial data ([Geopandas](https://github.com/geopandas/geopandas)).
- **Rasterio**: For reading and writing raster datasets ([Rasterio](https://github.com/mapbox/rasterio)).
- **Shapely**: For geometric operations like intersections and unions ([Shapely](https://github.com/shapely/shapely)).
- **Fiona**: For reading and writing vector geospatial data ([fiona](https://github.com/Toblerity/Fiona)).
- **xarray**: For handling multidimensional geospatial datasets ([xarray](https://github.com/pydata/xarray)).

### **Machine Learning Libraries**
- **TorchGeo**: Python deep learning lib for geospatial data ([TorchGeo](https://github.com/microsoft/torchgeo/))
- **scikit-learn**: Classic ML library for classification, regression, and clustering ([Scikit-learn](https://github.com/scikit-learn/scikit-learn)).
- **TensorFlow / PyTorch**: For deep learning tasks like image segmentation ([TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/)).
- **LightGBM / XGBoost**: Gradient boosting libraries for tabular geospatial datasets ([LightGBM](https://lightgbm.readthedocs.io/), [XGBoost](https://xgboost.readthedocs.io/)).

### **Visualization Tools**
- **Leaflet**: 🍃 JavaScript library for mobile-friendly interactive maps ([Leaflet](https://github.com/Leaflet/Leaflet))
- **Folium**: Create interactive maps ([Folium](https://github.com/python-visualization/folium)).
- **Kepler.gl**: Web-based tool for large-scale geospatial visualizations ([Kepler.gl](https://github.com/keplergl/kepler.gl)).
- **Deck.gl**: High-performance 3D geospatial visualizations ([Deck.gl](https://github.com/visgl/deck.gl)).
---
##  🌍GeoSpatial Tech Stack
<table> <tr> <!-- LEFT COLUMN --> <td style="vertical-align:top; width:50%; padding-right:12px;">

  <h3>Transform</h3>
  <table>
    <tr><th>Tool</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>GDAL</td><td>Core geospatial I/O, reprojection, raster/vector ops</td><td>🧰</td></tr>
    <tr><td>seer.ai</td><td>Data prep/ETL with geo context</td><td>🔮</td></tr>
    <tr><td>dbt</td><td>SQL-based transformations/versioned models</td><td>🧱</td></tr>
    <tr><td>Airbyte</td><td>Connectors for syncing data sources</td><td>🔌</td></tr>
    <tr><td>BigGeo</td><td>Large-scale geo ETL pipelines</td><td>🌏📦</td></tr>
    <tr><td>A5</td><td>Workflow utilities for data engineering</td><td>🛠️</td></tr>
  </table>

  <h3>Analytics</h3>
  <table>
    <tr><th>Tool</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>CARTO</td><td>Cloud location analytics & APIs</td><td>🗺️</td></tr>
    <tr><td>Fused</td><td>Unified geospatial analytics workspace</td><td>🧪</td></tr>
    <tr><td>Foursquare (FSQ)</td><td>POI, movement, visitation analytics</td><td>📍</td></tr>
    <tr><td>Hex</td><td>Notebooks + apps for data teams</td><td>🧮</td></tr>
    <tr><td>kepler.gl</td><td>High-performance geo viz in browser</td><td>🧭</td></tr>
    <tr><td>Preset</td><td>Managed Apache Superset</td><td>🎛️</td></tr>
    <tr><td>Apache Superset</td><td>BI dashboards, SQL exploration</td><td>📊</td></tr>
  </table>

  <h3>GIS</h3>
  <table>
    <tr><th>Tool</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>QGIS</td><td>Desktop GIS (edit, analyze, visualize)</td><td>🧭🖥️</td></tr>
    <tr><td>Felt</td><td>Collaborative web GIS mapping</td><td>🧩</td></tr>
    <tr><td>Atlas</td><td>Lightweight map design/hosting</td><td>🗺️✨</td></tr>
    <tr><td>NextGIS</td><td>GIS stack & services</td><td>🧱🗺️</td></tr>
  </table>

  <h3>AI</h3>
  <table>
    <tr><th>Tool</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>Klarety</td><td>GeoAI insights from messy geo data</td><td>🧠🗺️</td></tr>
    <tr><td>Monarcha</td><td>ML for EO/RS workflows</td><td>🦋</td></tr>
    <tr><td>CONTOUR</td><td>Foundation models for maps/imagery</td><td>🗺️🤖</td></tr>
    <tr><td>Bunting Labs</td><td>Geo dev tools / APIs</td><td>🐦</td></tr>
    <tr><td>aino</td><td>AI copilots for spatial ops</td><td>🤖</td></tr>
    <tr><td>Mundi</td><td>Earth data access + analytics</td><td>🌍</td></tr>
    <tr><td>GeoRetina</td><td>Vision models for remote sensing</td><td>👁️🛰️</td></tr>
    <tr><td>AskEarth</td><td>Natural-language Q&A over Earth data</td><td>💬🌎</td></tr>
  </table>

  <h3>Python</h3>
  <table>
    <tr><th>Tool</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>GeoPandas</td><td>Vector dataframes & spatial ops</td><td>🐼🗺️</td></tr>
    <tr><td>rasterio</td><td>Raster I/O (GDAL bindings)</td><td>🧾🛰️</td></tr>
    <tr><td>TorchGeo</td><td>PyTorch datasets/models for EO</td><td>🔥🌍</td></tr>
    <tr><td>leafmap</td><td>Jupyter interactive maps</td><td>🍃</td></tr>
    <tr><td>geemap</td><td>Earth Engine + geospatial viz</td><td>🗺️🔧</td></tr>
    <tr><td>lonboard</td><td>WebGL vector map rendering</td><td>🧭⚡</td></tr>
  </table>

  <h3>Formats</h3>
  <table>
    <tr><th>Format</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>GeoParquet</td><td>Columnar vectors with geo metadata</td><td>📦🗺️</td></tr>
    <tr><td>COG (Cloud-Optimized GeoTIFF)</td><td>HTTP-friendly rasters</td><td>☁️🖼️</td></tr>
    <tr><td>STAC</td><td>Cataloging EO assets</td><td>🗂️</td></tr>
    <tr><td>COPC.io (point clouds)</td><td>Streamable point clouds</td><td>☁️📍</td></tr>
    <tr><td>Zarr</td><td>Chunked n-D arrays (cloud-native)</td><td>🧱📚</td></tr>
  </table>

  <h3>Apps</h3>
  <table>
    <tr><th>Tool</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>Mapbox</td><td>Maps, tiles, SDKs</td><td>🗺️📦</td></tr>
    <tr><td>deck.gl</td><td>GPU-powered web viz</td><td>🧊</td></tr>
    <tr><td>MapLibre</td><td>Open map renderers (GL/Native)</td><td>🗺️🆓</td></tr>
    <tr><td>geobase</td><td>Location SDK/utilities</td><td>🧩📍</td></tr>
    <tr><td>Veda</td><td>NASA/USG EO visualization</td><td>🛰️📽️</td></tr>
  </table>

  <h3>Orchestrate</h3>
  <table>
    <tr><th>Tool</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>Apache Airflow</td><td>DAG-based scheduling</td><td>🌬️</td></tr>
    <tr><td>Astronomer</td><td>Managed Airflow</td><td>🌠</td></tr>
    <tr><td>dagster</td><td>Data orchestration & assets</td><td>🕸️</td></tr>
    <tr><td>kestra</td><td>Declarative workflows</td><td>🏗️</td></tr>
    <tr><td>Prefect</td><td>Pythonic orchestration</td><td>✅</td></tr>
  </table>

  <h3>Processing</h3>
  <table>
    <tr><th>Tool</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>Wherobots</td><td>Cloud-native spatial analytics</td><td>🤖🗺️</td></tr>
    <tr><td>Coiled</td><td>Managed Dask at scale</td><td>🌀</td></tr>
    <tr><td>Databricks</td><td>Lakehouse + Spark ML</td><td>🔥💎</td></tr>
    <tr><td>Apache Sedona</td><td>Spatial SQL on Spark</td><td>🗺️🔥</td></tr>
    <tr><td>Dask</td><td>Parallel Python</td><td>🧩⚡</td></tr>
    <tr><td>Apache Spark</td><td>Distributed compute</td><td>🔥</td></tr>
  </table>

  <h3>OLAP (Analytical)</h3>
  <table>
    <tr><th>Tool</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>Snowflake</td><td>Cloud data warehouse</td><td>❄️</td></tr>
    <tr><td>MotherDuck</td><td>Serverless DuckDB</td><td>🦆👩‍🍼</td></tr>
    <tr><td>DuckDB</td><td>In-process analytics</td><td>🦆</td></tr>
    <tr><td>Google BigQuery</td><td>Serverless DW + GIS</td><td>🔎📦</td></tr>
    <tr><td>Amazon Redshift</td><td>AWS DW</td><td>🟥</td></tr>
    <tr><td>Trino</td><td>SQL query engine (federation)</td><td>🚀</td></tr>
  </table>

  <h3>Catalogs / Tables</h3>
  <table>
    <tr><th>Tool</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>Apache Iceberg</td><td>Open table format</td><td>🧊</td></tr>
    <tr><td>Delta Lake</td><td>ACID tables on data lakes</td><td>🔺</td></tr>
    <tr><td>Earthmover</td><td>Geo data cataloging/ETL</td><td>🚚🌍</td></tr>
    <tr><td>DuckLake</td><td>DuckDB-native lakehouse tables</td><td>🦆🌊</td></tr>
  </table>

  <h3>Cloud Storage</h3>
  <table>
    <tr><th>Tool</th><th>What it’s for</th><th>Icon</th></tr>
    <tr><td>Amazon S3</td><td>Object storage</td><td>🪣</td></tr>
    <tr><td>Google Cloud Storage</td><td>Object storage</td><td>☁️🪣</td></tr>
    <tr><td>Azure Storage</td><td>Blobs/files/queues</td><td>🔷🪣</td></tr>
    <tr><td>Wasabi</td><td>S3-compatible storage</td><td>🌶️🪣</td></tr>
    <tr><td>Cloudflare R2 / Backblaze-style</td><td>Low-egress object storage</td><td>🌀🪣</td></tr>
    <tr><td>obstore</td><td>S3-compatible OSS</td><td>📦🪣</td></tr>
  </table>

</td>

</tr> </table>

---

## **🧭 Geospatial Fundamentals Cheat Sheet**

<table>
  <thead>
    <tr>
      <th style="text-align:left;">Concept</th>
      <th style="text-align:left;">Why it matters</th>
      <th style="text-align:left;">Learn more</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Raster data</strong></td>
      <td>Pixel/grid representation of continuous surfaces (imagery, elevation).</td>
      <td><a href="https://pro.arcgis.com/en/pro-app/latest/help/data/imagery/introduction-to-raster-data.htm">ArcGIS Pro — Raster data</a></td>
    </tr>
    <tr>
      <td><strong>Vector data</strong></td>
      <td>Points/lines/polygons for discrete features (roads, parcels).</td>
      <td><a href="https://support.esri.com/en-us/gis-dictionary/vector">Esri GIS Dictionary — Vector</a></td>
    </tr>
    <tr>
      <td><strong>Raster vs Vector</strong></td>
      <td>Know when to use each model for analysis and storage.</td>
      <td><a href="https://gisgeography.com/spatial-data-types-vector-raster/">GISGeography — Data types</a></td>
    </tr>
    <tr>
      <td><strong>Coordinate Reference System (CRS)</strong></td>
      <td>Defines how coordinates map to Earth; essential for accuracy.</td>
      <td><a href="https://proj-tmp.readthedocs.io/en/docs/about.html">PROJ — About CRS</a></td>
    </tr>
    <tr>
      <td><strong>EPSG codes</strong></td>
      <td>Standard identifiers for CRSs (e.g., 4326, 3857).</td>
      <td><a href="https://pyproj4.github.io/pyproj/stable/api/proj.html">pyproj — CRS reference</a></td>
    </tr>
    <tr>
      <td><strong>WGS84 / Lat-Lon (EPSG:4326)</strong></td>
      <td>Global geographic CRS used widely in data exchange.</td>
      <td><a href="https://en.wikipedia.org/wiki/Mercator_projection#Identifiers_(Web_Mercator_notes_include_EPSG:4326_context)">Wikipedia — EPSG:4326</a></td>
    </tr>
    <tr>
      <td><strong>Web Mercator (EPSG:3857)</strong></td>
      <td>Web mapping projection (Google/OSM tiles).</td>
      <td><a href="https://en.wikipedia.org/wiki/Web_Mercator_projection">Wikipedia — Web Mercator</a></td>
    </tr>
    <tr>
      <td><strong>UTM</strong></td>
      <td>Projected CRS in 6° zones for low-distortion mapping.</td>
      <td><a href="https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system">Wikipedia — UTM</a></td>
    </tr>
    <tr>
      <td><strong>Map projections (Mercator)</strong></td>
      <td>Transform globe to flat map; understand distortion.</td>
      <td><a href="https://www.britannica.com/science/Mercator-projection">Britannica — Mercator projection</a></td>
    </tr>
    <tr>
      <td><strong>GeoTIFF</strong></td>
      <td>Georeferenced raster format standard.</td>
      <td><a href="https://www.ogc.org/publications/standard/geotiff/">OGC — GeoTIFF</a></td>
    </tr>
    <tr>
      <td><strong>Cloud-Optimized GeoTIFF (COG)</strong></td>
      <td>GeoTIFF layout optimized for HTTP range reads.</td>
      <td><a href="https://www.cogeo.org/">COG — Specification</a></td>
    </tr>
    <tr>
      <td><strong>GeoPackage (.gpkg)</strong></td>
      <td>SQLite-based container for vector/rasters/tiles.</td>
      <td><a href="https://www.ogc.org/publications/standard/geopackage/">OGC — GeoPackage</a></td>
    </tr>
    <tr>
      <td><strong>Shapefile</strong></td>
      <td>Legacy vector format (SHP/SHX/DBF triplet).</td>
      <td><a href="https://www.esri.com/content/dam/esrisites/sitecore-archive/Files/Pdfs/library/whitepapers/pdfs/shapefile.pdf">Esri — Shapefile whitepaper</a></td>
    </tr>
    <tr>
      <td><strong>GeoJSON</strong></td>
      <td>JSON-based vector data format/spec.</td>
      <td><a href="https://datatracker.ietf.org/doc/html/rfc7946">IETF RFC 7946</a></td>
    </tr>
    <tr>
      <td><strong>MBTiles</strong></td>
      <td>SQLite container for tiled maps (raster/vector).</td>
      <td><a href="https://github.com/mapbox/mbtiles-spec">Mapbox — MBTiles spec</a></td>
    </tr>
    <tr>
      <td><strong>GeoParquet</strong></td>
      <td>Columnar (Parquet) storage with geospatial metadata.</td>
      <td><a href="https://geoparquet.org/releases/v1.1.0/">GeoParquet v1.1.0</a></td>
    </tr>
    <tr>
      <td><strong>NetCDF</strong></td>
      <td>Self-describing array format used for climate/EO.</td>
      <td><a href="https://docs.unidata.ucar.edu/netcdf-c/current/">Unidata — NetCDF</a></td>
    </tr>
    <tr>
      <td><strong>HDF5</strong></td>
      <td>High-performance hierarchical scientific data format.</td>
      <td><a href="https://support.hdfgroup.org/documentation/hdf5/latest/_intro_h_d_f5.html">The HDF Group — HDF5 intro</a></td>
    </tr>
    <tr>
      <td><strong>GDAL</strong></td>
      <td>Core library/CLI for raster &amp; vector I/O and transforms.</td>
      <td><a href="https://gdal.org/">GDAL documentation</a></td>
    </tr>
    <tr>
      <td><strong>gdalwarp (reproject/warp)</strong></td>
      <td>Reprojection, resampling, mosaicking.</td>
      <td><a href="https://gdal.org/en/stable/programs/gdalwarp.html">GDAL — gdalwarp</a></td>
    </tr>
    <tr>
      <td><strong>Resampling methods</strong></td>
      <td>Nearest, bilinear, cubic, lanczos, average, etc.</td>
      <td><a href="https://gdal.org/en/stable/programs/gdal_raster_resize.html">GDAL — raster resize</a></td>
    </tr>
    <tr>
      <td><strong>PROJ / pyproj</strong></td>
      <td>Geodetic/projection transforms in code.</td>
      <td><a href="https://pyproj4.github.io/pyproj/stable/api/proj.html">pyproj — PROJ API</a></td>
    </tr>
    <tr>
      <td><strong>GeoPandas</strong></td>
      <td>Pandas + geometry for vector data in Python.</td>
      <td><a href="https://geopandas.org/en/v0.9.0/getting_started/introduction.html">GeoPandas — Introduction</a></td>
    </tr>
    <tr>
      <td><strong>Spatial joins (GeoPandas)</strong></td>
      <td>Combine layers by spatial relationships.</td>
      <td><a href="https://geopandas.org/en/stable/gallery/spatial_joins.html">GeoPandas — Spatial joins</a></td>
    </tr>
    <tr>
      <td><strong>Shapely</strong></td>
      <td>Geometry objects &amp; operations (buffer, dissolve…).</td>
      <td><a href="https://github.com/shapely/shapely">Shapely repository</a></td>
    </tr>
    <tr>
      <td><strong>Rasterio</strong></td>
      <td>Python raster I/O built on GDAL.</td>
      <td><a href="https://media.readthedocs.org/pdf/rasterio/latest/rasterio.pdf">Rasterio — Docs PDF</a></td>
    </tr>
    <tr>
      <td><strong>Xarray</strong></td>
      <td>Labeled N-D arrays (great for EO/gridded time series).</td>
      <td><a href="https://docs.xarray.dev/">xarray documentation</a></td>
    </tr>
    <tr>
      <td><strong>rioxarray</strong></td>
      <td>Geo-enhancements for Xarray (CRS, transform, IO).</td>
      <td><a href="https://corteva.github.io/rioxarray/">rioxarray documentation</a></td>
    </tr>
    <tr>
      <td><strong>PDAL &amp; LAS</strong></td>
      <td>Point-cloud processing &amp; LAS point format spec.</td>
      <td><a href="https://pdal.io/">PDAL docs</a> · <a href="https://www.asprs.org/wp-content/uploads/2019/07/LAS_1_4_r15.pdf">ASPRS — LAS 1.4</a></td>
    </tr>
    <tr>
      <td><strong>WMS (OGC)</strong></td>
      <td>Request map images (rendered rasters) via web.</td>
      <td><a href="https://www.ogc.org/standards/wms/">OGC — WMS</a></td>
    </tr>
    <tr>
      <td><strong>WMTS (OGC)</strong></td>
      <td>Tiled map service for fast web maps.</td>
      <td><a href="https://www.ogc.org/standards/wmts/">OGC — WMTS</a></td>
    </tr>
    <tr>
      <td><strong>WFS (OGC)</strong></td>
      <td>Web access to actual vector features.</td>
      <td><a href="https://www.ogc.org/publications/standard/wfs/">OGC — WFS</a></td>
    </tr>
    <tr>
      <td><strong>STAC</strong></td>
      <td>Common spec to catalog/discover spatiotemporal assets.</td>
      <td><a href="https://stacspec.org/">STAC specification</a></td>
    </tr>
    <tr>
      <td><strong>Sentinel-2 (MSI)</strong></td>
      <td>13-band optical imagery (10/20/60 m).</td>
      <td><a href="https://documentation.dataspace.copernicus.eu/Data/Sentinel2.html">Copernicus — Sentinel-2</a></td>
    </tr>
    <tr>
      <td><strong>Sentinel-1 (SAR)</strong></td>
      <td>C-band radar; day/night, cloud-penetrating.</td>
      <td><a href="https://step.esa.int/docs/tutorials/S1TBX%20SAR%20Basics%20Tutorial.pdf">ESA — Sentinel-1 SAR basics</a></td>
    </tr>
    <tr>
      <td><strong>Landsat program</strong></td>
      <td>Long-running US optical EO archive.</td>
      <td><a href="https://www.usgs.gov/landsat-missions">USGS — Landsat missions</a></td>
    </tr>
    <tr>
      <td><strong>SRTM DEM</strong></td>
      <td>Global elevation (void-filled) dataset.</td>
      <td><a href="https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-shuttle-radar-topography-mission-srtm">USGS — SRTM</a></td>
    </tr>
    <tr>
      <td><strong>Copernicus DEM</strong></td>
      <td>Global DSM (GLO-30/90), GeoTIFF/DTED.</td>
      <td><a href="https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM">Copernicus — DEM</a></td>
    </tr>
    <tr>
      <td><strong>NDVI</strong></td>
      <td>Vegetation “greenness” index (NIR-Red)/(NIR+Red).</td>
      <td><a href="https://www.earthdata.nasa.gov/topics/land-surface/normalized-difference-vegetation-index-ndvi">NASA Earthdata — NDVI</a></td>
    </tr>
    <tr>
      <td><strong>NDWI (Gao 1996)</strong></td>
      <td>Vegetation water content index (NIR-SWIR)/(NIR+SWIR).</td>
      <td><a href="https://www.sciencedirect.com/science/article/pii/S0034425796000673">ScienceDirect — NDWI</a></td>
    </tr>
    <tr>
      <td><strong>NBR</strong></td>
      <td>Burn severity index (NIR-SWIR)/(NIR+SWIR).</td>
      <td><a href="https://www.usgs.gov/landsat-missions/landsat-normalized-burn-ratio">USGS — NBR</a></td>
    </tr>
    <tr>
      <td><strong>Cloud masking (QA60)</strong></td>
      <td>Sentinel-2 bitmask for clouds/cirrus (used in GEE).</td>
      <td><a href="https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED">Google Earth Engine — Sentinel-2 SR</a></td>
    </tr>
    <tr>
      <td><strong>Zonal statistics</strong></td>
      <td>Summarize raster values over polygons.</td>
      <td><a href="https://pythonhosted.org/rasterstats/">rasterstats — Zonal stats</a></td>
    </tr>
    <tr>
      <td><strong>Spatial autocorrelation (Moran’s I)</strong></td>
      <td>Detect clustering/dispersion in spatial data.</td>
      <td><a href="https://geodacenter.github.io/workbook/5a_global_auto/lab5a.html">GeoDa — Moran’s I</a></td>
    </tr>
    <tr>
      <td><strong>Tobler’s First Law</strong></td>
      <td>“Near things are more related than distant things.”</td>
      <td><a href="https://en.wikipedia.org/wiki/Tobler%27s_first_law_of_geography">Wikipedia — Tobler’s law</a></td>
    </tr>
    <tr>
      <td><strong>MAUP</strong></td>
      <td>Bias from aggregating data into arbitrary zones.</td>
      <td><a href="https://en.wikipedia.org/wiki/Modifiable_areal_unit_problem">Wikipedia — MAUP</a></td>
    </tr>
    <tr>
      <td><strong>Reprojection</strong></td>
      <td>Change dataset CRS to align analyses/maps.</td>
      <td><a href="https://gdal.org/en/stable/programs/gdal_raster_reproject.html">GDAL — raster reproject</a></td>
    </tr>
    <tr>
      <td><strong>Rescaling &amp; resampling</strong></td>
      <td>Change raster resolution methodically.</td>
      <td><a href="https://gdal.org/en/stable/programs/gdal_raster_resize.html">GDAL — raster resize</a></td>
    </tr>
    <tr>
      <td><strong>PostGIS</strong></td>
      <td>Spatial SQL in PostgreSQL (geometry/geography + ops).</td>
      <td><a href="https://postgis.net/docs/">PostGIS documentation</a></td>
    </tr>
    <tr>
      <td><strong>QGIS</strong></td>
      <td>Open-source desktop GIS (editing, analysis, viz).</td>
      <td><a href="https://docs.qgis.org/latest/en/docs/user_manual/index.html">QGIS user manual</a></td>
    </tr>
    <tr>
      <td><strong>STAC in practice</strong></td>
      <td>How agencies expose catalogs (example implementation).</td>
      <td><a href="https://www.usgs.gov/landsat-missions/spatiotemporal-asset-catalog-stac">USGS — STAC example</a></td>
    </tr>
  </tbody>
</table>

---

## **🎓 Courses to Learn Geospatial and Machine Learning**

### **Free Courses**
1. **Introduction to GIS**  
   - [Esri’s GIS Basics](https://www.esri.com/training/catalog/5d9cd7de5edc347a71611ccc/gis-basics/) 
   - [QGIS Tutorials](https://docs.qgis.org/latest/en/docs/index.html)

2. **Satellite Image Processing** 
   - [Bhuvan Satellite Dataset-Aerial Image Semantic Segmentation](https://www.kaggle.com/code/aletbm/aerial-image-for-semantic-segmentation)
   - [Google Earth Engine Tutorials](https://developers.google.com/earth-engine/tutorials)  
   - [NASA ARSET Remote Sensing Training](https://appliedsciences.nasa.gov/arset)

4. **Machine Learning Essentials**  
   - [FastAI’s Deep Learning for Coders](https://course.fast.ai/) (includes image classification tasks that can be applied to geospatial data).  
   - [Machine Learning with Python by Coursera](https://www.coursera.org/learn/machine-learning-with-python)

### **Paid Courses**
1. **Advanced GIS and Remote Sensing**  
   - [Coursera: GIS, Mapping, and Spatial Analysis Specialization](https://www.coursera.org/specializations/gis-mapping-spatial-analysis)  
   - [Udemy: Python for Geospatial Analysis](https://www.udemy.com/course/python-for-geospatial-analysis-gis/)  

2. **Deep Learning for Geospatial Applications**  
   - [Deep Learning for Satellite Imagery by AWS](https://aws.amazon.com/machine-learning/learn/satellite-imagery/)  
   - [Omdena’s Geospatial AI Courses](https://omdena.com/)  

---
# Machine Learning for Remote Sensing (ML4RS) Workshop @ ICLR 2024 [Microsoft Sponsor](https://www.microsoft.com/en-us/research/project/geospatial-machine-learning/)
This is a curated list of papers presented at the **Machine Learning for Remote Sensing (ML4RS)** Workshop at **ICLR 2023 & 2024**.


| **Title**                                                                                               | **Presentation Type** | **Award**          |
|---------------------------------------------------------------------------------------------------------|-----------------------|--------------------|
| [**Good at Captioning, Bad at Counting: Benchmarking GPT-4V on Earth Observation Data**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/16.pdf) | Oral                  | Best Paper         |
| [**A Concise Tiling Strategy for Preserving Spatial Context in Earth Observation Imagery**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/28.pdf) | Poster                | Best Poster        |
| [**Causal Graph Neural Networks for Wildfire Danger Prediction**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/16.pdf) | Oral                  |                    |
| [**Sparsely Labeled Land Cover Classification with Oversegmentation-based Graph U-Nets**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/16.pdf) | Oral                  |                    |
| [**Uncertainty Aware Tropical Cyclone Wind Speed Estimation from Satellite Data**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/16.pdf) | Oral                  |                    |
| [**CromSS: Cross-Modal Pre-Training with Noisy Labels for Remote Sensing Image Segmentation**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/23.pdf) | Oral                  |                    |
| [**Leveraging Synthetic Data and Machine Learning for Cloud Optical Thickness Estimation**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/16.pdf) | Oral                  |                    |
| [**Global Aboveground Biomass Density Estimation from Sentinel-2 Imagery**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/45.pdf) | Poster                |                    |
| [**AI-Powered School Mapping and Connectivity Status Prediction Using Satellite Imagery**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/24.pdf) | Poster                |                    |
| [**Evaluating Tool-Augmented Agents in Remote Sensing Platforms**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/65.pdf) | Poster                |                    |
| [**A Change Detection Reality Check**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/46.pdf) | Poster                |                    |
| [**Uncertainty Quantification for Probabilistic Machine Learning in Earth Observation**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/6.pdf) | Poster                |                    |
| [**Red Teaming Models for Hyperspectral Image Analysis Using Explainable AI**](https://ml-for-rs.github.io/iclr2024/camera_ready/papers/32.pdf) | Poster                |                    |

---

# Machine Learning for Remote Sensing (ML4RS) Workshop @ ICLR 2023

| **Title**                                                                                               | **Presentation Type** |
|---------------------------------------------------------------------------------------------------------|-----------------------|
| [**Towards Explainable Land Cover Mapping: A Counterfactual-Based Strategy**](https://arxiv.org/pdf/2301.01520.pdf) | Oral                  |
| [**Enhancing Acoustic Classification Using Meta-Data**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/9.pdf) | Oral                  |
| [**Explaining Multimodal Data Fusion: Occlusion Analysis for Wilderness Mapping**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/10.pdf) | Oral                  |
| [**Mask Conditional Synthetic Satellite Imagery**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/11.pdf) | Oral                  |
| [**Optimizing Ecosystem Monitoring through Machine Learning**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/12.pdf) | Oral                  |
| [**Aerial View Localization with Reinforcement Learning: Towards Emulating Search-and-Rescue**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/13.pdf) | Poster                |
| [**Improved Marine Debris Detection in Satellite Imagery with an Automatic Refinement of Coarse Hand Annotations**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/14.pdf) | Poster                |
| [**Titan Cloud Identification with Deep Transfer Learning**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/15.pdf) | Poster                |
| [**Evaluation Challenges for Geospatial ML**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/16.pdf) | Poster                |
| [**Building Light Models with Competitive Performance for Remote Sensing**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/17.pdf) | Poster                |
| [**Unsupervised Domain Adaptation for Semantic Segmentation of Dwellings with Unbalanced Optimal Transport**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/18.pdf) | Poster                |
| [**Efficient Ship Detection on Large Open Sea Areas**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/19.pdf) | Poster                |
| [**Remote Control: Debiasing Remote Sensing Predictions for Causal Inference**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/20.pdf) | Poster                |
| [**Improve State-Level Wheat Yield Forecasts in Kazakhstan on GEOGLAM’s EO Data by Leveraging a Simple Spatial-Aware Technique**](https://ml-for-rs.github.io/iclr2023/camera_ready/papers/21.pdf) | Poster                |

---

---
## **📁 Repository Contents [New additions are WIP]**

- **📂 Datasets**: Curated datasets for geospatial ML experiments.
- **📂 Tutorials**: Step-by-step guides and example notebooks.
- **📂 Notebooks**: Jupyter notebooks demonstrating geospatial machine learning workflows (1 in-repo quickstart).
- **📂 Notebooks/earthengine**: Vendored Google Earth Engine workflows (cloud masking, classification, change detection) sourced from the community — 42 notebooks across:
  - `CloudMasking` (4) · `RasterProcessing` (8) · `ArrayAnalytics` (4) · `VectorAndZonal` (4) · `SpatialJoins` (1)
  - `ImageCollections` (3) · `Segmentation` (1) · `Detection` (1) · `MachineLearning` (4)
  - `Terrain` (3) · `WaterMonitoring` (4) · `ChangeMonitoring` (2) · `Visualization` (3)
- **📂 Tools**: Scripts and utilities for geospatial data processing.

---

## **🤝 Contributing**

We welcome contributions! Whether you want to add a new resource, share a dataset, or submit a tutorial, here’s how you can help:  
1. Fork the repository.  
2. Create a new branch for your changes.  
3. Submit a pull request with a detailed description.

---
## Show your support
Give a 🌟 if this repo helped you! 

## **📞 Contact**

For questions, suggestions, or collaborations, feel free to open an issue or connect with me at:  
- Email: [sache.meet@yahoo.com]  
- LinkedIn: [www.linkedin.com/in/curious-susant]


```bibtex
@misc{Curious Susant,
    author       = {S Susant Achary},
    title        = {Machine-Learning-for-Geospatial},
    year         = {2025}
}
```
