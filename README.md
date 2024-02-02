# Blink And You Miss It
This project is a comprehensive pipeline designed to detect and assist drivers in identifying incoming traffic signs in a highway-like setup. The project employs a multi-stage approach involving four classifiers to enhance the accuracy and speed of traffic sign recognition.

Pipeline Overview
Traffic Sign Detection:

The first classifier determines whether each snapshot of a video contains a traffic sign or not.
Region of Interest (ROI) Cropping:

Upon detection, the pipeline utilizes a Region of Interest (ROI) technique to crop the relevant portion of the image containing the traffic sign.
Type Classification:

The cropped image is then fed into a binary classifier to distinguish between diagram-based and text-based traffic signs.
Text-Based Traffic Sign Recognition (OCR):

If the traffic sign is identified as text-based, an Optical Character Recognition (OCR) model is employed to extract the textual information.
Diagram-Based Traffic Sign Recognition:

For diagram-based signs, a specialized classifier is implemented to accurately recognize the specific sign.
Model Transfer and Weights Sharing
To enhance robustness and achieve faster outputs, the project emphasizes the transfer of weights between models. This transfer learning approach aids in leveraging knowledge gained from one model for the training of another, ultimately improving overall accuracy.

Integration of Preexisting Models
Blink-And-You-Miss-It is committed to achieving high accuracy by implementing well-established Convolutional Neural Network (CNN) architectures, including AlexNet, ResNet, and others. The incorporation of these preexisting models aims to explore various strategies for traffic sign recognition, pushing the boundaries of accuracy and efficiency.

Getting Started
To use Blink-And-You-Miss-It, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/Blink-And-You-Miss-It.git
Install dependencies:

Copy code
pip install -r requirements.txt
Run the pipeline:

css
Copy code
python main.py
Contributing
Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, feel free to open an issue or submit a pull request.
