# Video-Prediction  
- This app takes, as a parameter, a path of a video in which the robotic hand tries to grasp an object.   
- This app uses a CNN to classify each frame in a video into a successful try or not.  
- If frames in the last few seconds are classified as successful, it returns True with a graph which shows the value of each frame after being classified. Otherwise, it returns False with a graph.  

# Installation
1. Clone this repository.  
2. Download the model in this link, https://drive.google.com/open?id=1_rVIcU6sBRS321dwnTO3htf83C7p3jY3, and include it in the same directory as this repository was cloned.  
    - This model was built on a pre-trained model Inception ResNet V2. Details are discussed in https://github.com/u0953009/Binary-Classifier.  
3. Install requirements. `pip install -r requirements.txt`  

# Usage  
`$ python predict.py <video_file_path>`  

# Result  
Running with an example video will return 'True' with the graph below.  
`$ python predict.py example-video/2018-04-29-114407350.webm`  
<img src="https://github.com/u0953009/images/blob/master/video/Figure_1.png">    

