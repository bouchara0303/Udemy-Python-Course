import cv2, time

#Create Haar Cascade classifiers and start video capture
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
videoStream = cv2.VideoCapture(0)

#Video capture loop
while True:
    check, frame = videoStream.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,
    scaleFactor=1.3,
    minNeighbors=4)
    eyes = eyeCascade.detectMultiScale(frame,
    scaleFactor=1.3,
    minNeighbors=4)

    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 5)
        frame = cv2.putText(frame, "Face", (int((x + w) / 2), y - 15), cv2.FONT_HERSHEY_TRIPLEX, 5, (0,0,255))
    for x,y,w,h in eyes:
        frame = cv2.circle(frame, (int(x + w / 2), int(y + h / 2)), int(w / 2), (0, 255, 0), 5)
        frame = cv2.putText(frame, "Eye", (int((x + w)), y - 5), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,255,0))
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#End capture
videoStream.release()
cv2.destroyAllWindows()
