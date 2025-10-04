# Geospatial AI Multi Domain Scenarios (Open Data + Open Models) with Hugging Face Models

Below is a list of **40** practical scenarios with an example **use case**, a typical **open data source**, and an **open model/baseline** to start with.



> 📝 Most models are general baselines; for taking Live/production, fine-tune on your Area Of Interest /dataset and add geospatial post-processing (cloud/shadow masking, polygonization, topology cleanup).

| Scenario | Usecase | Data Source | Deep\ML Model (Open Source Hugging Face) |
|---|---|---|---|
| Agricultural field boundary extraction | Auto-delineate field polygons | Sentinel-2 L2A | `ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL` (foundation for segmentation) |
| Interactive field delineation | Click/prompt-based masks for fast labeling | Sentinel-2 (any raster) | `facebook/sam-vit-huge` (use via SAMGeo/Geo-SAM) |
| Crop-type mapping (per-parcel) | Classify crop per field | HLS/Sentinel-2 + polygons | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M-multi-temporal-crop-classification` |
| Multi-temporal field boundaries | Seasonal-robust parcel masks | Sentinel-2 time-series | `ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL` (temporal finetune) |
| Irrigation detection | Irrigated vs rainfed fields | S1 SAR + S2 | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (finetune for binary seg.) |
| Yield prediction | Parcel/regional yield | S2 + weather/soil | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (sequence regression head) |
| Weed detection (UAV) | Crop–weed recognition | UAV RGB | `ultralytics/ yolov8n` (finetune on DeepWeeds or field data) |
| Phenology / crop calendar | Sowing/harvest windows | S2 NDVI stacks | `earthflow/DOFA` (multimodal EO foundation; finetune for temporal cls.) |
| Surface water extent | Seasonal/permanent water | Landsat / S2 | `ibm-granite/granite-geospatial-uki-flooddetection` (water/flood seg.) |
| Rapid flood mapping | Inundation masks for response | Sentinel-2 / Sen1Floods11 | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M-sen1floods11` |
| Burned area mapping | Monthly burned area | MODIS / S2 | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (finetune for burned-area seg.) |
| Active fire detection | Hotspot QA/triage | MODIS/VIIRS | `facebook/dinov2-base` (feature extractor + shallow classifier) |
| Drought monitoring | Vegetation stress anomalies | MODIS/S2 | `ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL` (temporal anomaly head) |
| Building footprint extraction | Buildings at scale | SpaceNet / VHR | `KyanChen/BuildingExtraction` (STTNet) |
| Global open buildings reuse | QA/merge footprints | MS/Google Open Buildings | `facebook/dinov2-base` (vector features for QA) |
| Road extraction | Road centerlines/masks | DeepGlobe / VHR | `spectrewolf8/aerial-image-road-segmentation-with-U-NET-xp` |
| Urban change detection | New construction, expansion | SpaceNet-7 | `manuelhorveydaniel/ChangeFormer` |
| Power grid inference | Likely distribution lines | Night Lights + OSM | `facebook/dinov2-base` (feature extractor for heuristics) |
| Rooftop solar suitability | PV potential per roof | Lidar/DSM + footprints | `openmmlab/upernet-convnext-small` (roof facets segmentation) |
| Urban heat island (LST) | Heat risk hotspots | MODIS LST | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (regression head for LST proxy) |
| Aerosol / AQ proxy | PM proxy, smoke tracking | MAIAC AOD + meteo | `ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL` (spatiotemporal reg.) |
| Mangrove extent & change | Coastal ecosystem mapping | GMW / S2 | `IGNF/FLAIR-INC_rgbie_15cl_resnet34-unet` (LCZ/land-cover seg.) |
| Glacier outlines | Glacier inventory/change | Landsat/S2 | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (finetune on glacier masks) |
| Built-up / settlements | Urban extent | GHSL / S2 | `IGNF/FLAIR-INC_rgbie_15cl_resnet34-unet` |
| Nighttime lights analytics | Economic activity proxy | VIIRS NTL | `facebook/dinov2-base` (embedding + regressor) |
| Coral bleaching monitoring | Reef health alerts | Allen Coral Atlas | `openmmlab/upernet-convnext-small` (reef class seg.; finetune) |
| Ship detection (SAR) | Maritime surveillance | Sentinel-1 SAR | `mayrajeo/marine-vessel-detection-yolov8` (optical S2) or finetune YOLO on `ConnorLuckettDSTG/SARFish` |
| Fishing effort & presence | Likely fishing activity | AIS + S2/S1 | `ultralytics/yolov8n` (detector on S2; fuse with AIS rules) |
| Shoreline change | Erosion/accretion | Landsat/S2 | `openmmlab/upernet-convnext-small` (binary shoreline seg.) |
| Road passability (post-disaster) | Blocked/clear roads | VHR + flood layers | `spectrewolf8/aerial-image-road-segmentation-with-U-NET-xp` (finetune multiclass) |
| Damage assessment (buildings) | Post-event damage grades | xBD pre/post pairs | `manuelhorveydaniel/ChangeFormer` (damage change head) |
| Landslide susceptibility | Likely landslide zones | DEM + rain + S1/S2 | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (multimodal features + classifier) |
| Open traffic speed | Speed analytics | GPS → OSM | `facebook/dinov2-base` (embedding for road type/surface inference) |
| Surface water quality proxy | Turbidity/algal blooms | S2 coastal bands | `ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL` (regression on in-situ) |
| Aquaculture pond detection | Shrimp/fish ponds | S2 / VHR | `openmmlab/upernet-convnext-small` (pond seg.; refine to polygons) |
| Poverty/economic mapping | Socio-economic proxies | NTL + GHSL | `facebook/dinov2-base` (embedding + regressor) |
| Fire risk mapping | Exposure/recurrence | MODIS + LULC | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (risk classifier) |
| Coastline class mapping | Sand/rock/mud types | Landsat/S2 | `IGNF/FLAIR-INC_rgbie_15cl_resnet34-unet` (multiclass coastal LULC) |
| Global coastline extraction | Median-tide coastline | VHR/S2 | `openmmlab/upernet-convnext-small` (edge seg. + vectorization) |
| Vessel detections (SAR) | Non-AIS activity hints | S1 SAR | finetune `ultralytics/yolov8n` on `ConnorLuckettDSTG/SARFish` |
| Offshore infrastructure | Platforms/pipelines | S1/S2 + AIS context | `ultralytics/yolov8n` (object detector; custom labels) |
| Oil spill / slick detection (SAR) | Slick presence/extent | Sentinel-1 SAR | `MeghanaK25/sar-oil-slick-detection` |

---


