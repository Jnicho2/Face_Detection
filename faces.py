import cv2, sys

## The Haar cascades that I have chosen to use are loaded.

face_cascade = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_smile.xml')

"""
-------------------------------------------------------------------------------
detect - Detects faces in the video and draws boxes around features
-------------------------------------------------------------------------------
"""

def detect ():
    
    vid = cv2.VideoCapture (sys.argv[2])

    while ( vid.isOpened() ):
        
        rect, img = vid.read()

	## After loading the frame into img it checks that an image was loaded
	## if not the the video is unloaded and the loop ends

        if img is not None:

	    ## It creates a grayscale copy of the original image and uses the
	    ## faces haar cascade loaded at the top to find faces in the image. 
 
            gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale (gray, 1.3, 5)

            for (x, y, w, h) in faces:

		## For every face found it draws a green box around it.

                cv2.rectangle (img, (x,y), (x+w, y+h), (0, 255, 0), 2)

		## Using the values stored in face two new images are created
		## from the grayscaled and original image of the frame.

                face_gray = gray [y:y+h, x:x+w]
                face_color = img[y:y+h, x:x+w]

		## These face images are then checked for eyes and mouths and
		## borders are drawn around any found.

                eyes = eye_cascade.detectMultiScale (face_gray)
                mouths = mouth_cascade.detectMultiScale (face_gray)

                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle (face_color, (ex,ey), 
				   (ex+ew, ey+eh), (255, 0, 0), 1)
                for (mx,my,mw,mh) in mouths:
                    cv2.rectangle (face_color, (mx,my), (mx+mw,my+mh), 
				   (0, 0, 255), 1)

            cv2.imshow ('Detect Faces', img)

            ## If the user has hit the ESC key the loop ends
            if cv2.waitKey(1) & 0xFF == 27:
                vid.release ()
        else:
            vid.release ()		

    cv2.destroyAllWindows ()

"""
-------------------------------------------------------------------------------
blur - Detects faces and blurs them
-------------------------------------------------------------------------------
"""

def blur ():
    
    vid = cv2.VideoCapture (sys.argv[2])

    while ( vid.isOpened() ):

        rect, img = vid.read ()

        if img is not None:     

            gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale (gray, 1.3, 5)

	    ## After finding the faces in the image this will create a blurred
	    ## image in the area that the faces were detected and then put
	    ## the blur onto the original image in the same place.

            for (x, y, w, h) in faces:
                face = cv2.blur (img[y:y+h, x:x+w], (100, 100))
                img[y:y+face.shape[0], x:x+face.shape[1]] = face

            cv2.imshow ('Blur Faces', img)
            
            if cv2.waitKey(1) & 0xFF == 27:
                vid.release ()

        else:
            vid.release ()

    cv2.destroyAllWindows ()

"""
-------------------------------------------------------------------------------
The program runs a simple if statement to to make sure that enough arguements 
have been supplied by the user. Then another if statement that will run the 
correct function depending on what the user has entered into the command line.
-------------------------------------------------------------------------------
"""

if len(sys.argv) < 3:
    sys.stderr.write("No enough arguements were given\n")
    sys.exit (1)


if (sys.argv[1] == "blur"):
    blur()
elif (sys.argv[1] == "detect"):
    detect()
else :
    sys.stderr.write("Please enter blur or detect with the file name\n")


"""
End of program
-------------------------------------------------------------------------------
"""
