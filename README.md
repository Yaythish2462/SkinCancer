# SkinCancer Analysis using Deep Neural Networks

Skin cancer is among the most common and deadly cancers, marked by rapid, uncontrolled cell division in the skin. Early diagnosis is crucial for reducing fatalities, but accurate identification of different cancer types can be challenging, leading to potential misdiagnoses. This study proposes a framework utilizing the latest compact YOLO models—YOLOv3tiny, YOLOv4tiny, YOLOv5s, YOLOv7tiny, and YOLOv8s—to detect and classify nine types of skin cancer using the ISIC datasets. Results show that YOLOv5s and YOLOv8s excel in detecting different cancer classes. A fusion strategy combining predictions from both models improves overall accuracy, boosting mean average precision (mAP@0.5) from 91.5% to 94.3% and precision from 89.6% to 97.87%. The framework is tested on an Nvidia Jetson Nano for real-time performance, with inference times ranging from 13.9 ms to 142.5 ms per image across the models.

# Here is the Detailed analysis of the steps followed:

## Data collection

The data that is used in the project consists of nine types of skin cancer typically Actinic Keratosis, Basal Cell Carcinoma, Dermatofibroma, Melanoma, Nevus, Pigmented Benign Keratosis, Seborrheic Keratosis, Squamous Cell Carcinoma, and Vascular Lesion

The dataset can be downloaded here : [Download here](https://challenge.isic-archive.com/data/)

To install all the requirements packages run

```bash
pip install -r requirements.txt
```
