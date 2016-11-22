import cv2
import sys
import os

def count_faces(file):
    # Get user supplied values
    imagePath = file
    #print(os.walk('/Users/erikrudie/desktop/code/FaceDetect'))
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
                                         gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(30, 30)
                                         )

    print("Found {0} faces!".format(len(faces)))



for subdir, dirs, files in os.walk('/Users/erikrudie/desktop/code/FaceDetect/filter_here'):
    for file in files:
        print(file)
        filepath = subdir + os.sep + file

        if filepath.endswith((".png", ".jpg")):
            try:
                count_faces(filepath)
            except: # catch *all* exceptions
                e = sys.exc_info()[0]
                print( "<p>Error: %s</p>" % e )

