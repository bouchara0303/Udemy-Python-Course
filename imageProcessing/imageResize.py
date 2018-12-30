import cv2
import os

#List of files in current working directory
images = os.listdir(os.getcwd())
acceptedFormats = ('.jpg', '.jpeg', '.png')

#Checks if file in the list is an accepted format, then resizes it to 100x100
i = 0
while i < len(images):
    image = False
    for format in acceptedFormats:
        if format in images[i]:
            image = True
    if not image:
        del images[i]
    else:
        img = cv2.imread(images[i], -1)
        resized = cv2.resize(img, (100, 100))
        file, fileExtension = os.path.splitext(images[i])
        cv2.imwrite(('resizedImage' + str(i) + fileExtension), resized)
        i = i + 1
