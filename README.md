# Face_Detection
A short python script to detect faces in videos

This script is used to detect faces in video files and depending on the input 
supplied by the user it will either draw boxes around the face, mouth and eyes
or blur the face.

This script uses OpenCV to open and detect face/facial features in images.

OpenCV can be installed following the steps here:
https://pypi.org/project/opencv-python/

On Windows the script can be run using a command window and entering either of the
following commands:
	python faces.py detect myvideo
	python faces.py blur myvideo
	
where myvideo is replaced with the video file name. I've included a short stock 
video in this folder called test.mp4.
Whilst the program is playing a video the user can press the ESC key on the 
keyboard to stop the program early.

Some parts of this code have been adapted from code available in the OpenCV
documentation.
