import cv2, time

#Create haar cascade classifier and start video capture
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
videoStream = cv2.VideoCapture(0)

#Video capture loop
while True:
    check, frame = videoStream.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,
    scaleFactor=1.2,
    minNeighbors=5)

    if faces.any():
        for x,y,w,h in faces:
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 5)
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#End capture
videoStream.release()
cv2.destroyAllWindows()
