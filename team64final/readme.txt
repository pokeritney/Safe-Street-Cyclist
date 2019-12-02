1. DESCRIPTION - Describe the package in a few paragraphs
   
   All of our data used to display the final findings are preprocessed. The original data files used to train our model are in /CODE/Data folder. We saved all the steps to process our data in /CODE/Scripts folder. 

   Our dataset of bicycle collisions are downloaded from Transbase Database.They are saved  under /CODE/Data. Our Google Street View pictures of San Francisco, CA are downloaded from Google Cloud API. The code used to obtain GSV pictures is in /CODE/Scripts/streetViewAPI.py. And the step to register for Google Cloud API is in GSV_register.txt.

   In /CODE/Image_detect contains our trained Random Forest model to calculate our final composite risk score of each street of San Francisco, CA. The python script of trained model is named Open_Image_V4_Object_Detection-inception_resnet_v2.ipynb. Our composite risk score for each street of San Francisco is saved in Safe_score_segment.csv, where y2_Scaled is our final score used to visualize in the interface. In /CODE/image_detect/Trained_CNN_Model contains our trained CNN model to evaluate street safety, this model was served as a validation approach. 

   In /CODE/Viz, index.html is our constructed web app to display our visualization of the data and findings. /Viz/lib contains all the api library files we use. /Viz/static contains all the static files, such as csv/geojson. Please see 2 to access this web app.


2. INSTALLATION - How to install and setup your code

   A. Please navigate to directory: ~/team64final/CODE/Viz
   In the command shell, run the following command:
   $ python -m http.server

   B. This will set up a local host in your computer. A local server address will appear in the shell, copy that address and paste it into your browser address. (Note: Please use Firefox to view this website). In case no address is displayed, enter http://0.0.0.0:8000/index.html. Hit enter, you are then in Safe Street for Cyclist's interface.


3. EXECUTION - How to run a demo on your code
[Optional, but recommended] DEMO VIDEO - Include the URL of a 1-minute *unlisted* YouTube video in this txt file. The video would show how to install and execute your system/tool/approach (e.g, from typing the first command to compile, to system launching, and running some examples). Feel free to speed up the video if needed (e.g., remove less relevant video segments). This video is optional (i.e., submitting a video does not increase scores; not submitting one does not decrease scores). However, we recommend teams to try and create such a video, because making the video helps teams better think through what they may want to write in the README.txt, and generally how they want to "sell" their work.
