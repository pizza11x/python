import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"
# Create the haar cascade, it is just an xml file that contains the data to detect faces
faceCascade = cv2.CascadeClassifier(cascPath)
# Read image and convert it to grayscale
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
# General function that detects objects
# -gray is the grayscale image
# -scaleFactor
# -detection algorithm uses a moving window to detects objects
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces".format(len(faces)))
# x and y are the locations of the rectangle, w and h are width and height
for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image and wait for the user key
cv2.imshow("Faces found", image)
cv2.waitKey(0)
