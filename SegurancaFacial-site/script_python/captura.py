import cv2
import os

folder_name = "rostos"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

count = 0 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        face_roi = frame[y:y+h, x:x+w]

        img_name = f"{folder_name}/rosto_{count}.jpg"
        cv2.imwrite(img_name, face_roi)
        print(f"Imagem salva: {img_name}")
        count += 1

    cv2.imshow("Captura de Rostos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:  
        break

cap.release()
cv2.destroyAllWindows()
