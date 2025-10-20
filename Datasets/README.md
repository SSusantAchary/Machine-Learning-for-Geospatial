# Geospatial ML Datasets

Curated entry points for open geospatial datasets you can plug into machine learning workflows. Each entry includes a short description and the primary access method.

| Dataset | What you get | Access |
| --- | --- | --- |
| **Sentinel-2 Level-2A** | 10–60 m optical imagery with surface reflectance and cloud masks. | [Copernicus Data Space](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-2) |
| **Landsat Collection 2** | 30 m optical archive dating back to the 1980s. | [USGS EarthExplorer](https://earthexplorer.usgs.gov/) |
| **NAIP** | 1 m aerial imagery over the United States. | [USDA NAIP](https://www.fsa.usda.gov/programs-and-services/aerial-photography/imagery-programs/naip-imagery/) |
| **SRTM DEM** | 30 m global elevation. | [USGS SRTM](https://lpdaac.usgs.gov/products/srtmv003/) |
| **Copernicus DEM GLO-30** | 30 m digital surface model. | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM) |
| **OSM Geofabrik extracts** | City / country level vector data. | [Geofabrik Download](https://download.geofabrik.de/) |

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
