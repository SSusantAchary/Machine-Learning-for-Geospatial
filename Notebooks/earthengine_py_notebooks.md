# Earth Engine Python Notebook Picks

Curated notebooks from [`giswqs/earthengine-py-notebooks`](https://github.com/giswqs/earthengine-py-notebooks) that are now vendored under `Notebooks/earthengine/` for quick offline access. Each table links to the local copy (cloned on 2025-01-05) and notes the workflow they illustrate.

## Cloud Masking & Preprocessing

| Notebook | Focus | Local copy |
|---|---|---|
| Landsat 8 Surface Reflectance QA | Apply QA band filtering to clean Landsat 8 scenes. | [Open](earthengine/CloudMasking/landsat8_surface_reflectance.ipynb) |
| Landsat 8 TOA QA Mask | Decode the QA band for TOA reflectance masking. | [Open](earthengine/CloudMasking/landsat8_toa_qa_mask.ipynb) |
| Sentinel-2 Cloud Mask | Use scene classification (SCL) for Sentinel-2 cloud removal. | [Open](earthengine/CloudMasking/sentinel2_cloud_mask.ipynb) |
| Landsat Cloud Score | Score and threshold cloud probability via `px.cloudScore`. | [Open](earthengine/CloudMasking/landsat_cloud_score.ipynb) |

## Temporal Composites & Image Collections

| Notebook | Focus | Local copy |
|---|---|---|
| Creating Monthly Imagery | Build monthly composites from a multi-year collection. | [Open](earthengine/ImageCollections/creating_monthly_imagery.ipynb) |
| Calendar Range Filters | Filter collections by seasonal windows. | [Open](earthengine/ImageCollections/filtering_by_calendar_range.ipynb) |
| Expression Map | Evaluate custom expressions across an image collection. | [Open](earthengine/ImageCollections/expression_map.ipynb) |

## Raster Processing & Analysis

| Notebook | Focus | Local copy |
|---|---|---|
| Band Math | Compose custom spectral indices and ratios. | [Open](earthengine/RasterProcessing/band_math.ipynb) |
| Composite Bands | Merge multiband imagery into composite products. | [Open](earthengine/RasterProcessing/composite_bands.ipynb) |
| Conditional Operations | Apply conditional logic to raster pixels. | [Open](earthengine/RasterProcessing/conditional_operations.ipynb) |
| Connected Pixel Count | Label contiguous pixel groups for segmentation prep. | [Open](earthengine/RasterProcessing/connected_pixel_count.ipynb) |
| Sentinel-1 Filtering | Smooth SAR backscatter and mitigate speckle. | [Open](earthengine/RasterProcessing/sentinel1_filtering.ipynb) |
| Resampling & Resolution | Change pixel resolution with appropriate aggregation. | [Open](earthengine/RasterProcessing/resampling.ipynb) |
| Reduce Resolution | Downsample imagery while preserving statistics. | [Open](earthengine/RasterProcessing/reduce_resolution.ipynb) |
| Canny Edge Detector | Extract edges from imagery for boundary detection. | [Open](earthengine/RasterProcessing/canny_edge_detector.ipynb) |

## Array Analytics & Advanced Reducers

| Notebook | Focus | Local copy |
|---|---|---|
| Spectral Unmixing | Decompose pixels into fractional endmembers. | [Open](earthengine/ArrayAnalytics/spectral_unmixing.ipynb) |
| Linear Regression | Fit linear models using array reducers. | [Open](earthengine/ArrayAnalytics/linear_regression.ipynb) |
| Eigen Analysis | Compute eigenvalues/eigenvectors from raster arrays. | [Open](earthengine/ArrayAnalytics/eigen_analysis.ipynb) |
| Quality Mosaic | Build mosaics using per-pixel quality metrics. | [Open](earthengine/ArrayAnalytics/quality_mosaic.ipynb) |

## Vector Analysis & Zonal Stats

| Notebook | Focus | Local copy |
|---|---|---|
| Feature Buffering | Create distance buffers around vector features. | [Open](earthengine/VectorAndZonal/feature_buffer.ipynb) |
| Column Statistics by Group | Summarize attributes grouped by field values. | [Open](earthengine/VectorAndZonal/column_stats_by_group.ipynb) |
| Zonal Statistics (Image ➜ FeatureCollection) | Reduce raster values over polygons. | [Open](earthengine/VectorAndZonal/zonal_stats_image_region.ipynb) |
| Raster ➜ Vector Conversion | Convert raster classes to polygons for downstream ML. | [Open](earthengine/VectorAndZonal/raster_to_vector.ipynb) |

## Spatial Joins & Feature Linking

| Notebook | Focus | Local copy |
|---|---|---|
| Spatial Joins | Join features based on spatial relationships. | [Open](earthengine/SpatialJoins/spatial_joins.ipynb) |

## Terrain & Elevation Products

| Notebook | Focus | Local copy |
|---|---|---|
| SRTM Elevation | Access and visualize global SRTM DEM tiles. | [Open](earthengine/Terrain/srtm.ipynb) |
| HydroSHEDS DEM | Ingest HydroSHEDS hydrologically conditioned DEMs. | [Open](earthengine/Terrain/hydrosheds_dem.ipynb) |
| ALOS CHILI | Work with the ALOS global landform dataset. | [Open](earthengine/Terrain/alos_chili.ipynb) |

## Machine Learning & Classification

| Notebook | Focus | Local copy |
|---|---|---|
| CART Classifier | Train a CART supervised classifier on labeled imagery. | [Open](earthengine/MachineLearning/cart_classifier.ipynb) |
| SVM Classifier | Apply support vector machines to remote sensing features. | [Open](earthengine/MachineLearning/svm_classifier.ipynb) |
| Clustering | Perform unsupervised clustering (k-means-like) on spectral bands. | [Open](earthengine/MachineLearning/clustering.ipynb) |
| Confusion Matrix | Evaluate classifier accuracy with a confusion matrix. | [Open](earthengine/MachineLearning/confusion_matrix.ipynb) |
| Python Scripts | Companion scripts for batch execution. | [Browse](earthengine/MachineLearning/) |

## Segmentation & Detection

| Notebook | Focus | Local copy |
|---|---|---|
| SNIC Superpixels | Generate SNIC superpixels for downstream segmentation. | [Open](earthengine/Segmentation/segmentation_snic.ipynb) |
| Center Pivot Irrigation Detector | Detect circular irrigation fields via pattern recognition. | [Open](earthengine/Detection/center_pivot_irrigation_detector.ipynb) |

## Change Detection & Water Monitoring

| Notebook | Focus | Local copy |
|---|---|---|
| Global Surface Water — Occurrence | Map long-term water presence from the JRC dataset. | [Open](earthengine/WaterMonitoring/global_surface_water_occurrence.ipynb) |
| Global Surface Water — Change Intensity | Quantify water gain/loss over time. | [Open](earthengine/WaterMonitoring/global_surface_water_change_intensity.ipynb) |
| Global Surface Water — Class Transition | Analyze transitions between water/non-water classes. | [Open](earthengine/WaterMonitoring/global_surface_water_class_transition.ipynb) |
| NAIP NDWI Time Series | Derive NDWI trends from NAIP imagery. | [Open](earthengine/WaterMonitoring/naip_ndwi_timeseries.ipynb) |
| GLAD Deforestation Alerts | Monitor forest loss hotspots using GLAD alerts. | [Open](earthengine/ChangeMonitoring/glad_alert.ipynb) |
| Australia Bushfire Assessment | Inspect burn severity using Sentinel imagery. | [Open](earthengine/ChangeMonitoring/fire_australia.ipynb) |

## Visualization & Symbology

| Notebook | Focus | Local copy |
|---|---|---|
| RGB Composites | Build true/false-color composites with custom band ordering. | [Open](earthengine/Visualization/image_rgb_composite.ipynb) |
| Hillshade Rendering | Generate analytical hillshades from DEMs. | [Open](earthengine/Visualization/hillshade.ipynb) |
| Color Palettes | Apply and customize color palettes for raster display. | [Open](earthengine/Visualization/image_color_palettes.ipynb) |

> ℹ️ Each notebook remains licensed under the original repo’s terms (Apache-2.0). See `Notebooks/earthengine/README.md` for attribution guidance.
