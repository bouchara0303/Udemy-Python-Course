import cv2
import os

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Creates list of files and folders in current working directory
images = os.listdir(os.getcwd())
formats = ('.jpg', '.jpeg', '.png')

#Iterates through list to check if file is an accepted format
i=0
while i < len(images):
    image = False
    for format in formats:
        if format in images[i]:
            image = True
    if image:
        i = i+1
    else:
        del images[i]

#Iterates through list of images to detect
for image in images:
    img = cv2.imread(image, 1)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grey,
    scaleFactor=1.2,
    minNeighbors=5)

    for x,y,w,h in faces:
        img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 5)
    cv2.imshow(image, img)
    cv2.waitKey(0)
    cv2.destroyWindow(winname=image)
