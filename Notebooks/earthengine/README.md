# Earth Engine Notebook Bundle

This directory mirrors a curated subset of notebooks from [`giswqs/earthengine-py-notebooks`](https://github.com/giswqs/earthengine-py-notebooks) (commit `99fbc4a`, retrieved 2025-01-05). They are grouped by workflow to support geospatial machine learning experiments offline.

## Folders
- `CloudMasking/` — QA-based filters for Landsat and Sentinel-2 scenes.
- `ImageCollections/` — Temporal compositing utilities and expression maps.
- `RasterProcessing/` — Band math, resampling, SAR filtering, edge detection, and other raster transforms.
- `VectorAndZonal/` — Feature engineering helpers for polygons and zonal statistics.
- `ArrayAnalytics/` — Array-based linear algebra, spectral unmixing, and quality mosaics.
- `SpatialJoins/` — Example spatial join operations for feature collections.
- `Segmentation/` — Superpixel segmentation workflows (e.g., SNIC).
- `Detection/` — Domain-specific detectors such as center-pivot irrigation.
- `Terrain/` — Elevation products (SRTM, HydroSHEDS, ALOS).
- `WaterMonitoring/` — Surface-water occurrence/change tutorials plus NDWI trends.
- `ChangeMonitoring/` — Forest alert and bushfire assessment demos.
- `Visualization/` — RGB composites, hillshade, and palette styling guides.
- `MachineLearning/` — CART, SVM, clustering, and accuracy assessment workflows (with matching `.py` scripts).

## License
Original notebooks are Apache-2.0 licensed by the source repository. Keep headers intact when adapting or redistributing.
