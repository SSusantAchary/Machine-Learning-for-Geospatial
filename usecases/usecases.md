# Geospatial AI Multi Domain Scenarios (Open Data + Open Models) with Hugging Face Models

Below is a list of **40** practical scenarios with an example **use case**, a typical **open data source**, and an **open model/baseline** to start with.

> 📝 Most models are general baselines; for taking Live/production, fine-tune on your Area Of Interest / dataset and add geospatial post-processing (cloud/shadow masking, polygonization, topology cleanup).

| Scenario | Usecase | Data Source | Deep\ML Model (Open Source Hugging Face) |
|---|---|---|---|
| Agricultural field boundary extraction | Auto-delineate field polygons | Sentinel-2 L2A | `ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL` (foundation for segmentation) |
| Interactive field delineation | Click/prompt-based masks for fast labeling | Sentinel-2 (any raster) | `facebook/sam-vit-huge` (use via SAMGeo/Geo-SAM) |
| Crop-type mapping (per-parcel) | Classify crop per field | HLS/Sentinel-2 + polygons | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M-multi-temporal-crop-classification` |
| Multi-temporal field boundaries | Seasonal-robust parcel masks | Sentinel-2 time-series | `ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL` (temporal finetune) |
| Irrigation detection | Irrigated vs rainfed fields | Sentinel-1 SAR + Sentinel-2 | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (finetune for binary segmentation) |
| Yield prediction | Parcel/regional yield | Sentinel-2 + weather/soil | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (sequence regression head) |
| Weed detection (UAV) | Crop–weed recognition | UAV RGB | `ultralytics/yolov8n` (finetune on DeepWeeds or field data) |
| Phenology / crop calendar | Sowing/harvest windows | Sentinel-2 NDVI stacks | `earthflow/DOFA` (multimodal EO foundation; finetune for temporal classification) |
| Surface water extent | Seasonal/permanent water | Landsat / Sentinel-2 | `ibm-granite/granite-geospatial-uki-flooddetection` (water/flood segmentation) |
| Rapid flood mapping | Inundation masks for response | Sentinel-2 / Sen1Floods11 | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M-sen1floods11` |
| Burned area mapping | Monthly burned area | MODIS / Sentinel-2 | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (finetune for burned-area segmentation) |
| Active fire detection | Hotspot QA/triage | MODIS / VIIRS | `facebook/dinov2-base` (feature extractor + shallow classifier) |
| Drought monitoring | Vegetation stress anomalies | MODIS / Sentinel-2 | `ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL` (temporal anomaly head) |
| Building footprint extraction | Buildings at scale | SpaceNet / VHR | `KyanChen/BuildingExtraction` (STTNet) |
| Global open buildings reuse | QA/merge footprints | Microsoft / Google Open Buildings | `facebook/dinov2-base` (vector features for QA) |
| Road extraction | Road centerlines/masks | DeepGlobe / VHR | `spectrewolf8/aerial-image-road-segmentation-with-U-NET-xp` |
| Urban change detection | New construction, expansion | SpaceNet-7 | `manuelhorveydaniel/ChangeFormer` |
| Power grid inference | Likely distribution lines | Night Lights + OSM | `facebook/dinov2-base` (feature extractor for heuristics) |
| Rooftop solar suitability | PV potential per roof | LiDAR/DSM + footprints | `openmmlab/upernet-convnext-small` (roof facets segmentation) |
| Urban heat island (LST) | Heat risk hotspots | MODIS LST | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (regression head for LST proxy) |
| Aerosol / air-quality proxy | PM proxy, smoke tracking | MAIAC AOD + meteorology | `ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL` (spatiotemporal regression) |
| Mangrove extent & change | Coastal ecosystem mapping | Global Mangrove Watch / Sentinel-2 | `IGNF/FLAIR-INC_rgbie_15cl_resnet34-unet` (land-cover segmentation) |
| Glacier outlines | Glacier inventory/change | Landsat / Sentinel-2 | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (finetune on glacier masks) |
| Built-up / settlements | Urban extent | GHSL / Sentinel-2 | `IGNF/FLAIR-INC_rgbie_15cl_resnet34-unet` |
| Nighttime lights analytics | Economic activity proxy | VIIRS NTL | `facebook/dinov2-base` (embedding + regressor) |
| Coral bleaching monitoring | Reef health alerts | Allen Coral Atlas | `openmmlab/upernet-convnext-small` (reef class segmentation; finetune) |
| Ship detection (SAR) | Maritime surveillance | Sentinel-1 SAR | `mayrajeo/marine-vessel-detection-yolov8` (optical baseline) + finetune on `ConnorLuckettDSTG/SARFish` |
| Fishing effort & presence | Likely fishing activity | AIS + Sentinel-2/Sentinel-1 | `ultralytics/yolov8n` (detector + AIS fusion) |
| Shoreline change | Erosion/accretion monitoring | Landsat / Sentinel-2 | `openmmlab/upernet-convnext-small` (binary shoreline segmentation) |
| Road passability (post-disaster) | Blocked/clear roads | VHR + flood layers | `spectrewolf8/aerial-image-road-segmentation-with-U-NET-xp` (multiclass finetune) |
| Damage assessment (buildings) | Post-event damage grades | xBD pre/post pairs | `manuelhorveydaniel/ChangeFormer` (damage change head) |
| Landslide susceptibility | Likely landslide zones | DEM + rainfall + Sentinel-1/2 | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (multimodal classifier) |
| Open traffic speed | Speed analytics | GPS traces → OSM | `facebook/dinov2-base` (embedding for road attributes) |
| Surface water quality proxy | Turbidity/algal blooms | Sentinel-2 coastal bands | `ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL` (regression on in-situ data) |
| Aquaculture pond detection | Shrimp/fish ponds | Sentinel-2 / VHR | `openmmlab/upernet-convnext-small` (pond segmentation; polygonize) |
| Poverty/economic mapping | Socio-economic proxies | Nighttime lights + GHSL | `facebook/dinov2-base` (embedding + regressor) |
| Fire risk mapping | Exposure/recurrence | MODIS + land cover | `ibm-nasa-geospatial/Prithvi-EO-1.0-100M` (risk classifier) |
| Coastline class mapping | Sand/rock/mud types | Landsat / Sentinel-2 | `IGNF/FLAIR-INC_rgbie_15cl_resnet34-unet` (multi-class coastal LULC) |
| Global coastline extraction | Median-tide coastline | VHR / Sentinel-2 | `openmmlab/upernet-convnext-small` (edge segmentation + vectorization) |
| Vessel detections (SAR) | Non-AIS activity hints | Sentinel-1 SAR | `ultralytics/yolov8n` finetuned on `ConnorLuckettDSTG/SARFish` |
| Offshore infrastructure | Platforms/pipelines | Sentinel-1/Sentinel-2 + AIS context | `ultralytics/yolov8n` (object detector; custom labels) |
| Oil spill / slick detection (SAR) | Slick presence/extent | Sentinel-1 SAR | `MeghanaK25/sar-oil-slick-detection` |
