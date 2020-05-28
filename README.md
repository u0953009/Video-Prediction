# Video-Prediction  
- This app takes, as parameter, a path of a video in which the robotic hand tries to grasp an object.   
- This app uses a CNN to classfy each frame in a video whether a try was succesful or not.  
- If frames in the last few seconds are classified as successful, it returns True with a graph which shows the value of each frame after being classified. Otherwise, it returns False with a graph.  

# Installation
1. Clone this repository.  
2. Download https://drive.google.com/open?id=1hsHdJEUlV6NH4cqraq9sL9S0YpTrmgZt and include it in the same directory as this repository was cloned.  
3. Install requirements. `pip install -r requirements.txt`  

# Usage  
`$ python predict.py <video_file_path>`  

# Result  
Running with an example video will return 'True' with the graph below.  
`$ python predict.py example-video/2018-04-29-114407350.webm`  
<img src="https://github.com/u0953009/images/blob/master/video/Figure_1.png">    

