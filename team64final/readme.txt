1. DESCRIPTION - Describe the package in a few paragraphs
   
   All of our data used to display the final findings are preprocessed. The original data files used to train our model are in /CODE/Data folder. Since the street view pictures used to train the model are too big, we only show a few samples in /CODE/Data/GSV_downloads. Besides, we saved all the steps to process our data in /CODE/Scripts folder. 

   Our dataset of bicycle collisions are downloaded from TIMS & Transbase Database.They are saved under /CODE/Data. Our Google Street View pictures of San Francisco, CA are downloaded from Google Cloud API. The code used to obtain GSV pictures is in /CODE/Scripts/streetViewAPI.py. And the step to register for Google Cloud API is in /CODE/Scripts/GSV_register.txt.

   The training data, which are the risk scores we aggregated from the collision data and the street features data is /CODE/Data/model_data_segment_full_20191109.csv. The steps to process this data is in /CODE/Scripts/model_data_segment_full_20191109.py.

   In /CODE/Model contains our trained Random Forest model to calculate our final composite risk score of each street of San Francisco, CA. The python script of trained model is named Open_Image_V4_Object_Detection-inception_resnet_v2.ipynb. Our calculated composite risk score for each street of San Francisco is saved in /CODE/Data/Safe_score_segment.csv, where y2_Scaled is our final score are linearly color scaled to be used to visualize in the map. And each street segment coordinates, which used to map these street, are found by /CODE/Scripts/Segment_score_latlon.ipynb. 
   In /CODE/Model/CNN_Image_ZH1129.py contains our trained CNN model to evaluate street safety, this model was served as a validation approach. 

   In /CODE/Viz, index.html is our constructed web app to display our visualization of the data and findings. /Viz/lib contains all the api library files we use. /Viz/static contains all the static files, such as csv/geojson. Please see 2 to access this web app.


2. INSTALLATION - How to install and setup your code

   A. Please navigate to directory: ~/team64final/CODE/Viz
   In the command shell, run the following command:
   $ python -m http.server

   B. This will set up a local host in your computer. 
   (Note: Please use Firefox to view this website).
   A local server address will appear in the shell, copy that address and paste it into your browser address. In case no address is displayed, enter http://0.0.0.0:8000/index.html. Hit enter, you are then in Safe Street for Cyclist's website.


3. EXECUTION - How to run a demo on your code
[Optional, but recommended] DEMO VIDEO - Include the URL of a 1-minute *unlisted* YouTube video in this txt file. The video would show how to install and execute your system/tool/approach (e.g, from typing the first command to compile, to system launching, and running some examples). Feel free to speed up the video if needed (e.g., remove less relevant video segments). This video is optional (i.e., submitting a video does not increase scores; not submitting one does not decrease scores). However, we recommend teams to try and create such a video, because making the video helps teams better think through what they may want to write in the README.txt, and generally how they want to "sell" their work.
