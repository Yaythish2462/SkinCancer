# SkinCancer Analysis using Deep Neural Networks
<p align=justify>
Skin cancer is among the most common and deadly cancers, marked by rapid, uncontrolled cell division in the skin. Early diagnosis is crucial for reducing fatalities, but accurate identification of different cancer types can be challenging, leading to potential misdiagnoses. This study proposes a framework utilizing the latest compact YOLO models YOLOv3tiny, YOLOv4tiny, YOLOv5s, YOLOv7tiny, and YOLOv8s to detect and classify nine types of skin cancer using the ISIC datasets. Results show that YOLOv5s and YOLOv8s excel in detecting different cancer classes. A fusion strategy combining predictions from both models improves overall accuracy, boosting mean average precision mAP@0.5 from 91.5% to 94.3% and precision from 89.6% to 97.87%. The framework is tested on an Nvidia Jetson Nano for real-time performance, with inference times ranging from 13.9 ms to 142.5 ms per image across the models.
<p/>

# Here is the Detailed analysis of the steps followed:

- ## Data collection

<p align=justify>
The data that is used in the project consists of nine types of skin cancer typically Actinic Keratosis, Basal Cell Carcinoma, Dermatofibroma, Melanoma, Nevus, Pigmented Benign Keratosis, Seborrheic Keratosis, Squamous Cell Carcinoma, and Vascular Lesion.
<p/>

  The dataset can be downloaded here : [Download here](https://challenge.isic-archive.com/data/)

- ## Data PreProcessing

  After the data is downloaded in the link divide the dataset in the ratio of 70:20:10 for train,test and validation.

Create different folders as follows and import the data.

```bash
images
   |_ Train
   |_ Test
   |_ Valiadation
   
labels
   |_ Train
   |_ Test
   |_ Valiadation
```
Create a dataset.yaml file and import these codes,

```bash
train: r"Add full path to the train images"
test:  r"Add full path to the ttest images"
val: : r"Add full path to the validation images"

nc: "Number of classes in numbers eg. 9"
names: "class names with comma"
```
- ## Download all the YOLO Models

  - YOLOv3 : [Download here](https://github.com/ultralytics/yolov3)
  - YOLOv4 : [Download here](https://github.com/AlexeyAB/darknet)
  - YOLOv5 : [Download here](https://github.com/ultralytics/yolov5)
  - YOLOv7 : [Download here](https://github.com/WongKinYiu/yolov7)
  - YOLOv8 : [Download here](https://github.com/ultralytics/ultralytics)

Or use this code one by one:

```bash
git clone https://github.com/ultralytics/yolov3.git
git clone https://github.com/AlexeyAB/darknet.git
git clone https://github.com/ultralytics/yolov5.git
git clone https://github.com/WongKinYiu/yolov7.git
git clone https://github.com/ultralytics/ultralytics.git
```
- ## Model Training 

  Train all the repective models using the train.py file in each git repo accoring to the code in each of the YOLO git repo models and collect the weight files.

- ## Model Validation 

  After the model training run val.py file in each of the versions of yolo to get the validation data.

- ## Ensembling the Model

To ensemble the model clone this repository using,
```bash
git clone https://github.com/Yaythish2462/SkinCancer.git 
```
To install all the requirements packages for ensembling run

```bash
pip install -r requirements.txt
```

After cloning open ensemble.py file and replace thses things.

```bash
image_path = r"Image path of the particular image"
file_path_model1 = r"Validation txt label file of that same image of yolov5s model"
file_path_model2 = r"Validation txt label file of that same image of yolov8s model"
```
Run the file to get the ensembled model of YOLO for high accuracy.

## Overall Flow of the Process :
<p align="center">
<img src="https://vitalflux.com/wp-content/uploads/2022/08/Voting-ensemble-method-2.png" alt="image" width="300" height="auto">
<p/>

