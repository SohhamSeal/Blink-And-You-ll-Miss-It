# Blink And You'll Miss It!!
This project is a comprehensive pipeline designed to detect and assist drivers in identifying incoming traffic signs in a highway-like setup. The project employs a multi-stage approach involving four classifiers to enhance the accuracy and speed of traffic sign recognition.

## Pipeline Overview
![Pipeline](https://github.com/SohhamSeal/Blink-And-You-Miss-It/blob/main/Flow%20Diagrams/Overall%20Operation.png?raw=true)

### Traffic Sign Detection:
The first classifier determines whether each snapshot of a video contains a traffic sign or not.

### Region of Interest (ROI) Cropping:
Upon detection, the pipeline utilizes a Region of Interest (ROI) technique to crop the relevant portion of the image containing the traffic sign.

### Type Classification:
The cropped image is then fed into a binary classifier to distinguish between diagram-based and text-based traffic signs.

### Text-Based Traffic Sign Recognition (OCR):
If the traffic sign is identified as text-based, an Optical Character Recognition (OCR) model is employed to extract the textual information.

### Diagram-Based Traffic Sign Recognition:
For diagram-based signs, a specialized classifier is implemented to accurately recognize the specific sign.

#### Model Transfer and Weights Sharing
To enhance robustness and achieve faster outputs, the project emphasizes the transfer of weights between models. This transfer learning approach aids in leveraging knowledge gained from one model for the training of another, ultimately improving overall accuracy.

#### Integration of Preexisting Models
Blink-And-You-Miss-It is committed to achieving high accuracy by implementing well-established Convolutional Neural Network (CNN) architectures, including AlexNet, ResNet, and others. The incorporation of these preexisting models aims to explore various strategies for traffic sign recognition, pushing the boundaries of accuracy and efficiency.

## About the Datasets
### GTSRB - German Traffic Sign Recognition Benchmark [->](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)
The German Traffic Sign Benchmark is a multi-class, single-image classification challenge held at the International Joint Conference on Neural Networks (IJCNN) 2011. The benchmark has the following properties:
- Single-image, multi-class classification problem
- More than 40 classes
- More than 50,000 images in total
- Large, lifelike database

#### Acknowledgements
[INI Benchmark Website](http://benchmark.ini.rub.de/)

### Mapillary Traffic Sign Dataset [->](https://www.mapillary.com/dataset/trafficsign) 
Blink-And-You-Miss-It utilizes the Mapillary Traffic Sign Dataset, a diverse street-level imagery dataset with bounding box annotations for detecting and classifying traffic signs globally.

### Results
The following details were obtained on the dataset mentioned above:
____________________________
| Model         | Accuracy |
|---------------|----------|
| Classifier 1  | 91.5     |
| Classifier 2  | 97.24    |
| Classifier 3  | 99.98    |
| Classifier 4  | 95.49    |
| Overall Model | 89.8     |
|---------------|----------|

#### License:
By incorporating the Mapillary Traffic Sign Dataset, this project adheres to the Creative Commons Attribution NonCommercial Share Alike (CC BY-NC-SA) license. The usage of this dataset is in accordance with the CC BY-NC-SA license and the Mapillary Terms of Use.
