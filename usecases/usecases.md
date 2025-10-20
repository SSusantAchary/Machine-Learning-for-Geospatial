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

## Notebook References (By Domain)

Curated Hugging Face ecosystem notebooks to pair with the geospatial scenarios above.

### NLP — 20 notebooks

| Notebook | Code |
|---|---|
| 🖥️ Text classification (BERT/DistilBERT, PyTorch) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/text_classification.ipynb) |
| 🚀 Text classification (TF/Keras) | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_classification-tf.ipynb) |
| 🖥️ DistilBERT IMDB fine-tuning (HF Course) | [GitHub](https://github.com/huggingface/course/blob/main/chapter3/classification.ipynb) |
| 🚀 RoBERTa sentiment (GLUE SST-2) Trainer | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/pytorch/quicktour.ipynb) |
| 🖥️ Token classification / NER (BERT) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/token_classification.ipynb) |
| 🖥️ Question answering (SQuAD, BERT) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/question_answering.ipynb) |
| 🖥️ Summarization (T5/BART) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/summarization.ipynb) |
| 🖥️ Translation (Marian / Helsinki-NLP) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/translation.ipynb) |
| 🚀 Instruction-tuned FLAN-T5 generation | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_generation.ipynb) |
| 🚀 LoRA/QLoRA with PEFT (sequence classification) | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/peft/peft_training_text_classification.ipynb) |
| 🚀 LoRA/QLoRA for causal-LM (generation) | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/peft/peft_lora_int8_int4.ipynb) |
| 🖥️ Sentence-Transformers semantic search (all-MiniLM) | [Docs](https://www.sbert.net/examples/applications/semantic-search/README.html) |
| 🖥️ SBERT multilingual retrieval | [Docs](https://www.sbert.net/examples/applications/semantic-search/semantic_search_ml-qa/README.html) |
| 🖥️ bge-* embeddings quickstart | [Docs](https://github.com/FlagOpen/FlagEmbedding/blob/master/docs/text_embedding/quick_start_EN.md) |
| 🖥️ e5 embeddings & retrieval | [GitHub](https://github.com/intfloat/e5-mistral-7b-instruct#usage) |
| 🖥️ Reranking with mixedbread-ai / Cross-Encoders | [Docs](https://www.sbert.net/examples/applications/cross-encoder/README.html) |
| 🚀 DistilBERT QA (Trainer + evaluate) | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/question_answering-tf.ipynb) |
| 🚀 Pipeline zero-shot classification | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/pipeline_tutorial.ipynb) |
| 🖥️ Datasets streaming + tokenization (large corpora) | [GitHub](https://github.com/huggingface/course/blob/main/chapter5/processing.ipynb) |
| 🖥️ Evaluate metrics (accuracy/F1/ROUGE) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/evaluate.ipynb) |

### Vision — 20 notebooks

| Notebook | Code |
|---|---|
| 🖥️ ViT image classification (Imagenette) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/image_classification.ipynb) |
| 🖥️ CLIP zero-shot classification | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/zero_shot_image_classification.ipynb) |
| 🖥️ CLIP retrieval (text↔image) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/image_text_retrieval.ipynb) |
| 🖥️ DETR object detection (COCO-style) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/object_detection.ipynb) |
| 🖥️ SegFormer semantic segmentation | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/semantic_segmentation.ipynb) |
| 🚀 Mask2Former segmentation (HF example) | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/vision_mask2former.ipynb) |
| 🚀 SAM – Segment Anything demo | [Colab](https://colab.research.google.com/github/facebookresearch/segment-anything/blob/main/notebooks/automatic_mask_generator_example.ipynb) |
| 🚀 GroundingDINO open-vocabulary detection | [Colab](https://colab.research.google.com/github/IDEA-Research/GroundingDINO/blob/main/demo/GroundingDINO_Demo.ipynb) |
| 🚀 TrOCR OCR (printed text) | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/ocr.ipynb) |
| 🚀 Donut document understanding (OCR-free) | [Colab](https://colab.research.google.com/github/clovaai/donut/blob/master/demo.ipynb) |
| 🚀 DPT / MiDaS depth estimation | [Colab](https://colab.research.google.com/github/isl-org/MiDaS/blob/master/notebooks/midas.ipynb) |
| 🚀 Depth-Anything HF demo notebook | [Colab](https://colab.research.google.com/github/LiheYoung/Depth-Anything/blob/main/notebooks/depth_anything_v2_demo.ipynb) |
| 🚀 Pose estimation with MMPose + HF datasets | [Colab](https://colab.research.google.com/github/open-mmlab/mmpose/blob/main/demo/MMPose_Tutorial.ipynb) |
| 🖥️ Image feature extraction (ViT as encoder) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/image_feature_extraction.ipynb) |
| 🚀 BLIP image–text retrieval | [Colab](https://colab.research.google.com/github/salesforce/BLIP/blob/main/notebooks/demo.ipynb) |
| 🚀 LayoutLMv3 document layout tasks | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/layoutlmv3_document_ai.ipynb) |
| 🚀 Owl-ViT open-vocabulary detection | [Colab](https://colab.research.google.com/github/google-research/scenic/blob/main/scenic/projects/owl_vit/notebooks/OWLv2_demo.ipynb) |
| 🚀 Florence-2 zero-shot vision tasks | [Colab](https://colab.research.google.com/github/microsoft/Florence-2/blob/main/notebooks/florence2_demo.ipynb) |
| 🚀 Vision fine-tune with timm + HF | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/vision_timm_finetune.ipynb) |
| 🖥️ Diffusers image generation quickstart | [GitHub](https://github.com/huggingface/notebooks/blob/main/diffusers/stable_diffusion/stable_diffusion_intro.ipynb) |

### Audio — 20 notebooks

| Notebook | Code |
|---|---|
| 🖥️ Whisper tiny/base ASR (HF pipeline) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/automatic_speech_recognition.ipynb) |
| 🚀 Whisper fine-tuning (English subset) | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/asr_fine_tuning_whisper.ipynb) |
| 🖥️ wav2vec2 ASR (base-960h) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/wav2vec2_asr.ipynb) |
| 🚀 HuBERT audio classification (SUPERB) | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/audio_classification_superb.ipynb) |
| 🚀 Keyword spotting (Speech Commands) | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/keyword_spotting.ipynb) |
| 🚀 Speaker verification (ECAPA-TDNN, SpeechBrain) | [Colab](https://colab.research.google.com/github/speechbrain/speechbrain/blob/develop/recipes/VoxCeleb/SpeakerRec/SVECAPA.ipynb) |
| 🚀 Speaker diarization (pyannote) | [Colab](https://colab.research.google.com/github/pyannote/pyannote-audio/blob/develop/tutorials/diarization_api.ipynb) |
| 🚀 Audio emotion recognition (SUPERB ER) | [Colab](https://colab.research.google.com/github/superbbenchmark/superb/blob/master/notebook/SUPERB_ER_demo.ipynb) |
| 🚀 TTS (Coqui-TTS basic colab) | [Colab](https://colab.research.google.com/github/coqui-ai/TTS/blob/dev/notebooks/TTS_inference_demo.ipynb) |
| 🚀 Voice activity detection (pyannote VAD) | [Colab](https://colab.research.google.com/github/pyannote/pyannote-audio/blob/develop/tutorials/pipeline_demo.ipynb) |
| 🚀 WavLM ASR / embeddings demo | [Colab](https://colab.research.google.com/github/microsoft/unilm/blob/master/wavlm/notebooks/WavLM_Demo.ipynb) |
| 🚀 XLS-R multilingual ASR | [Colab](https://colab.research.google.com/github/patrickvonplaten/notebooks/blob/master/Fine_tune_XLSR_Wav2Vec2_on_Arabic_ASR_with_Common_Voice.ipynb) |
| 🚀 Audio tagging (UrbanSound8K with HF) | [Colab](https://colab.research.google.com/github/sanchit-gandhi/notebooks/blob/main/audio_classification_hf.ipynb) |
| 🚀 Streaming ASR with transformers | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/asr_streaming.ipynb) |
| 🚀 Textless NLP (HuBERT units) demo | [Colab](https://colab.research.google.com/github/facebookresearch/textlesslib/blob/main/notebooks/demo.ipynb) |
| 🚀 Music tagging with AST | [Colab](https://colab.research.google.com/github/qiuqiangkong/audioset_tagging_cnn/blob/master/colab/ast_audioset_demo.ipynb) |
| 🚀 Silero VAD + ASR integration | [Colab](https://colab.research.google.com/github/snakers4/silero-models/blob/master/examples/silero_vad_colab.ipynb) |
| 🚀 Audio augmentation & features (librosa) | [Colab](https://colab.research.google.com/github/musikalkemist/AudioSignalProcessingForML/blob/master/03-Audio-Data-Augmentation.ipynb) |
| 🚀 torchaudio pipeline tutorial | [Colab](https://colab.research.google.com/github/pytorch/tutorials/blob/main/beginner_source/audio_classifier_tutorial.ipynb) |
| 🚀 Audio to embeddings (CLAP/LAION) | [Colab](https://colab.research.google.com/github/LAION-AI/CLAP/blob/main/notebooks/CLAP_demo.ipynb) |

### Multimodal — 20 notebooks

| Notebook | Code |
|---|---|
| 🚀 BLIP image captioning (Salesforce) | [Colab](https://colab.research.google.com/github/salesforce/BLIP/blob/main/notebooks/demo.ipynb) |
| 🚀 BLIP-2 (OPT-2.7B) demo | [Colab](https://colab.research.google.com/github/salesforce/LAVIS/blob/main/projects/blip2/eval/blip2_eval_demo.ipynb) |
| 🖥️ CLIP retrieval (text↔image) | [GitHub](https://github.com/huggingface/notebooks/blob/main/examples/image_text_retrieval.ipynb) |
| 🚀 OWL-ViT open-vocabulary detection | [Colab](https://colab.research.google.com/github/google-research/scenic/blob/main/scenic/projects/owl_vit/notebooks/OWLv2_demo.ipynb) |
| 🚀 Qwen2-VL small demo notebook | [Colab](https://colab.research.google.com/github/QwenLM/Qwen2-VL/blob/main/notebooks/Qwen2_VL_Colab_Demo.ipynb) |
| 🚀 OpenFlamingo 3B demo | [Colab](https://colab.research.google.com/github/mlfoundations/open_flamingo/blob/main/notebooks/open_flamingo_vqa_demo.ipynb) |
| 🚀 LLaVA 1.5 demo (VLM chat) | [Colab](https://colab.research.google.com/github/haotian-liu/LLaVA/blob/main/docs/colab/llava_colab.ipynb) |
| 🚀 Kosmos-2 grounding demo | [Colab](https://colab.research.google.com/github/microsoft/unilm/blob/master/kosmos-2/notebooks/Kosmos-2_Demo.ipynb) |
| 🚀 Florence-2 multi-task vision-language | [Colab](https://colab.research.google.com/github/microsoft/Florence-2/blob/main/notebooks/florence2_demo.ipynb) |
| 🚀 ALBEF retrieval/captioning (LAVIS) | [Colab](https://colab.research.google.com/github/salesforce/LAVIS/blob/main/projects/albef/eval/albef_eval_demo.ipynb) |
| 🚀 ImageBind (audio-image-text) demo | [Colab](https://colab.research.google.com/github/facebookresearch/ImageBind/blob/main/notebooks/ImageBind_Demo.ipynb) |
| 🚀 CLIP Interrogator (caption from image) | [Colab](https://colab.research.google.com/github/pharmapsychotic/clip-interrogator/blob/main/clip_interrogator.ipynb) |
| 🚀 Video-Q&A (Video-LLaVA style) | [Colab](https://colab.research.google.com/github/LanguageBind/Video-LLaVA/blob/main/colab/Video-LLaVA-1.5-7B-colab.ipynb) |
| 🚀 Multimodal RAG with CLIP embeddings | [Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/multimodal_retrieval.ipynb) |
| 🚀 GroundingDINO + SAM pipeline | [Colab](https://colab.research.google.com/github/IDEA-Research/Grounded-Segment-Anything/blob/main/demo/Grounded_Segment_Anything.ipynb) |
| 🚀 Pix2Struct (screen-to-text) demo | [Colab](https://colab.research.google.com/github/google-research/pix2struct/blob/main/notebooks/pix2struct_colab_demo.ipynb) |
| 🚀 Donut + ViTSTR document VQA | [Colab](https://colab.research.google.com/github/clovaai/donut/blob/master/demo_docvqa.ipynb) |
| 🚀 CLAP multimodal audio-text retrieval | [Colab](https://colab.research.google.com/github/LAION-AI/CLAP/blob/main/notebooks/CLAP_demo.ipynb) |
| 🚀 BLIP-2 VQA eval (LAVIS) | [Colab](https://colab.research.google.com/github/salesforce/LAVIS/blob/main/projects/blip2/eval/vqa_eval.ipynb) |
| 🚀 MiniGPT-4 style demo (open variant) | [Colab](https://colab.research.google.com/github/Vision-CAIR/MiniGPT-4/blob/main/MiniGPT-4.ipynb) |
