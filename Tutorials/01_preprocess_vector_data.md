# Tutorial 01 — Preprocess Vector Data with GeoPandas

This walkthrough demonstrates a typical preprocessing routine for vector data ahead of machine learning feature engineering.

## Goals
- Load OpenStreetMap building footprints.
- Reproject to a local metric CRS.
- Generate geometric features (area, perimeter, compactness).
- Export the cleaned dataset.

## Steps

### 1. Install dependencies
```bash
pip install geopandas shapely pyproj
```

### 2. Load and inspect the data
```python
import geopandas as gpd

buildings = gpd.read_file("data/osm_buildings.geojson")
print(buildings.crs)
print(buildings.head())
```

### 3. Reproject to a local CRS
```python
LOCAL_EPSG = 32633  # UTM zone example; replace with your own.

buildings = buildings.to_crs(epsg=LOCAL_EPSG)
```

### 4. Engineer geometric features
```python
buildings["area_m2"] = buildings.geometry.area
buildings["perimeter_m"] = buildings.geometry.length
buildings["compactness"] = 4 * 3.14159 * buildings.area_m2 / buildings.perimeter_m.pow(2)
```

### 5. Export to GeoParquet
```python
buildings.to_parquet("data/osm_buildings_clean.parquet", index=False)
```

## Next steps
- Join with raster-derived statistics (e.g., NDVI) using `geopandas.sjoin`.
- Feed engineered features into a scikit-learn model for classification.
