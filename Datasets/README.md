# Geospatial ML Datasets

Curated entry points for open geospatial datasets you can plug into machine learning workflows. Each entry includes a short description and the primary access method.

| Dataset | What you get | Formats | Access |
| --- | --- | --- | --- |
| **Sentinel-2 Level-2A** | 10–60 m optical imagery with surface reflectance and cloud masks. | COG GeoTIFF, JP2 via ESA | [Copernicus Data Space](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-2) |
| **Landsat Collection 2** | 30 m optical archive dating back to the 1980s. | GeoTIFF, COG | [USGS EarthExplorer](https://earthexplorer.usgs.gov/) |
| **NAIP** | 1 m aerial imagery over the United States. | GeoTIFF, MrSID | [USDA NAIP](https://www.fsa.usda.gov/programs-and-services/aerial-photography/imagery-programs/naip-imagery/) |
| **SRTM DEM** | 30 m global elevation. | GeoTIFF, HGT | [USGS SRTM](https://lpdaac.usgs.gov/products/srtmv003/) |
| **Copernicus DEM GLO-30** | 30 m digital surface model. | GeoTIFF | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM) |
| **OSM Geofabrik extracts** | City / country level vector data. | Shapefile, GeoJSON, PBF | [Geofabrik Download](https://download.geofabrik.de/) |
| **Sentinel-1 GRD** | C-band SAR backscatter with VV/VH polarizations. | GeoTIFF (through export), SAFE | [Earth Engine Catalog](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD) |
| **MODIS MOD13Q1** | 16-day NDVI/EVI composites (250 m). | HDF, GeoTIFF (via export) | [Earth Engine Catalog](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD13Q1) |
| **JRC Global Surface Water** | Historical surface water occurrence and change. | GeoTIFF, GeoPackage | [Earth Engine Catalog](https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_4_YearlyHistory) |
| **ESA WorldCover 10m** | Global 10 m land-cover map (2021–2023). | COG GeoTIFF | [Earth Engine Catalog](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCover_v200) |
| **VIIRS Nighttime Lights** | Monthly global night lights (Day/Night Band). | HDF5, GeoTIFF (via export) | [Earth Engine Catalog](https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMCFG) |
| **USDA Cropland Data Layer** | Annual 30 m crop type classification (US). | GeoTIFF | [Earth Engine Catalog](https://developers.google.com/earth-engine/datasets/catalog/USDA_NASS_CDL) |

## 🔗 Dataset Tiles

<table>
  <tr>
    <td><a href="#sentinel-2-level-2a"><strong>Sentinel‑2 L2A</strong></a><br/><small>10–60 m optical SR</small></td>
    <td><a href="#sentinel-1-grd"><strong>Sentinel‑1 GRD</strong></a><br/><small>C-band SAR backscatter</small></td>
    <td><a href="#modis-mod13q1"><strong>MODIS MOD13Q1</strong></a><br/><small>16-day NDVI/EVI</small></td>
  </tr>
  <tr>
    <td><a href="#jrc-global-surface-water"><strong>JRC Surface Water</strong></a><br/><small>Water occurrence/change</small></td>
    <td><a href="#esa-worldcover-10m"><strong>ESA WorldCover</strong></a><br/><small>10 m land cover</small></td>
    <td><a href="#viirs-nighttime-lights"><strong>VIIRS Night Lights</strong></a><br/><small>Monthly radiance</small></td>
  </tr>
  <tr>
    <td><a href="#usda-cropland-data-layer"><strong>USDA CDL</strong></a><br/><small>US crop types</small></td>
    <td><a href="#osm-geofabrik-extracts"><strong>OSM Extracts</strong></a><br/><small>Vector features</small></td>
    <td><a href="#srtm-dem"><strong>SRTM DEM</strong></a><br/><small>30 m elevation</small></td>
  </tr>
</table>

## India Geospatial AI Scenario Catalog
<table>
  <tr>
    <td width="33%" valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Emblem_of_India.svg" width="240" height="160"><br/>
      <b>Survey of India — Nakshe</b><br/>
      Official topo sheets (1:50k/250k).<br/>
      <a href="https://soinakshe.nic.in/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-toposheets%20%7C%20vector%20%7C%20India-informational"/>
    </td>
    <td width="33%" valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Bhuvanlogo.jpg" width="240" height="160"><br/>
      <b>ISRO/NRSC — Bhuvan</b><br/>
      National geoportal: imagery & thematic layers.<br/>
      <a href="https://bhuvan.nrsc.gov.in/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-imagery%20%7C%20services%20%7C%20India-informational"/>
    </td>
    <td width="33%" valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/India_location_map.svg" width="240" height="160"><br/>
      <b>India-WRIS</b><br/>
      River basins, dams, hydrology layers.<br/>
      <a href="https://indiawris.gov.in/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-hydrology%20%7C%20vector%20%7C%20webgis-informational"/>
    </td>
  </tr>

  <tr>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Geological_Survey_of_India_Centenary_1951_stamp_of_India.jpg" width="240" height="160"><br/>
      <b>GSI — BhuKosh</b><br/>
      National geology maps (lithology, minerals).<br/>
      <a href="https://bhukosh.gsi.gov.in/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-geology%20%7C%20vector%20%7C%20maps-informational"/>
    </td>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/India%27s_forest_cover-_by_state_(percentage_of_land_area).png" width="240" height="160"><br/>
      <b>Forest Survey of India</b><br/>
      Forest cover, change, fire alerts dashboards.<br/>
      <a href="https://www.fsi.nic.in/">Site</a><br/>
      <img src="https://img.shields.io/badge/tags-forests%20%7C%20raster%20%7C%20vector-informational"/>
    </td>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Emblem_of_India.svg" width="240" height="160"><br/>
      <b>SLUSI — Soil & Land Use</b><br/>
      Soil/land capability & land-use planning maps.<br/>
      <a href="https://slusi.dac.gov.in/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-soils%20%7C%20landuse%20%7C%20vector-informational"/>
    </td>
  </tr>

  <tr>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Datagovin.svg" width="240" height="160"><br/>
      <b>Open Government Data — India</b><br/>
      Central catalog of open datasets (many GIS).<br/>
      <a href="https://data.gov.in/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-open--data%20%7C%20CSV%20%7C%20GIS-informational"/>
    </td>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Logo_of_the_Census_of_India.jpg" width="240" height="160"><br/>
      <b>Census of India (GIS)</b><br/>
      Administrative boundaries & demographics.<br/>
      <a href="https://censusindia.gov.in/census.website/">Site</a><br/>
      <img src="https://img.shields.io/badge/tags-admin%20boundaries%20%7C%20attributes-informational"/>
    </td>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Openstreetmap_logo.svg" width="240" height="160"><br/>
      <b>OpenStreetMap (India)</b><br/>
      Community roads, POIs, buildings; India extracts.<br/>
      <a href="https://www.openstreetmap.org/">OSM</a> • <a href="https://download.geofabrik.de/asia/india.html">India extract</a><br/>
      <img src="https://img.shields.io/badge/tags-OSM%20%7C%20vector%20%7C%20POI-informational"/>
    </td>
  </tr>

  <tr>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/mosdac_logo.jpg" width="240" height="160"><br/>
      <b>MOSDAC (ISRO)</b><br/>
      Meteorology & oceanography satellite data.<br/>
      <a href="https://mosdac.gov.in/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-weather%20%7C%20ocean%20%7C%20imagery-informational"/>
    </td>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/A_land_cover_map_of_the_HKH_region_was_developed_using_Landsat_30-meter_data..png" width="240" height="160"><br/>
      <b>NRSC — LULC (Bhuvan)</b><br/>
      India land-use/land-cover products (1:50k & updates).<br/>
      <a href="https://bhuvan.nrsc.gov.in/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-LULC%20%7C%20raster%20%7C%20vector-informational"/>
    </td>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Copernicus_Logo_240.png" width="240" height="160"><br/>
      <b>Copernicus (Sentinel)</b><br/>
      Sentinel-1/2/3 imagery via Data Space.<br/>
      <a href="https://dataspace.copernicus.eu/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-satellite%20%7C%20Sentinel%20%7C%20imagery-informational"/>
    </td>
  </tr>

  <tr>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/USGS_logo.svg" width="240" height="160"><br/>
      <b>USGS — EarthExplorer</b><br/>
      Landsat, SRTM, ASTER, more (India covered).<br/>
      <a href="https://earthexplorer.usgs.gov/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-Landsat%20%7C%20DEM%20%7C%20imagery-informational"/>
    </td>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/World_Topography.jpg" width="240" height="160"><br/>
      <b>OpenTopography</b><br/>
      Global/topical DEMs; LiDAR where available.<br/>
      <a href="https://opentopography.org/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-DEM%20%7C%20SRTM%20%7C%20ALOS-informational"/>
    </td>
    <td valign="top">
      <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Mystus_gulio.jpg" width="240" height="160"><br/>
      <b>India Biodiversity Portal</b><br/>
      Species occurrences & ecosystem layers.<br/>
      <a href="https://indiabiodiversity.org/">Portal</a><br/>
      <img src="https://img.shields.io/badge/tags-biodiversity%20%7C%20occurrence%20%7C%20points-informational"/>
    </td>
  </tr>
</table>


## Sample downloader

```python
#!/usr/bin/env python3
"""
Download a GeoTIFF tile via HTTP range requests using rasterio and rio-xarray.
Designed for Cloud-Optimized GeoTIFF (COG) sources.
"""

from pathlib import Path

import rasterio
from rasterio.session import AWSSession
from rasterio.vrt import WarpedVRT

COG_URL = "https://sentinel-cogs.s3.amazonaws.com/sentinel-s2-l2a-cogs/48/Q/WE/2020/9/S2B_48QWE_20200929_0_L2A/B04.tif"
OUTPUT = Path("sentinel2_red_band.tif")


def download_cog(url: str, output: Path) -> None:
    """Stream a COG to disk without downloading the full scene."""
    session = AWSSession()  # Falls back to anonymous; edit for authenticated buckets.
    with rasterio.Env(session=session):
        with rasterio.open(url) as src, WarpedVRT(src) as vrt:
            data = vrt.read()
            profile = vrt.profile

    output.parent.mkdir(parents=True, exist_ok=True)
    with rasterio.open(output, "w", **profile) as dst:
        dst.write(data)


if __name__ == "__main__":
    download_cog(COG_URL, OUTPUT)
    print(f"Saved {OUTPUT.resolve()}")
```

> ℹ️ The example above uses an anonymous AWS session. Replace `COG_URL` with any public COG to try it out.
