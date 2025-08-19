import cv2
import face_recognition
import os

folder_name = "rostos"

known_encodings = []
known_names = []

print("Carregando imagens conhecidas...")

for filename in os.listdir(folder_name):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        path = os.path.join(folder_name, filename)

        image = face_recognition.load_image_file(path)

        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(filename.split(".")[0]) 
            print(f"Imagem {filename} carregada.")
        else:
            print(f"Nenhum rosto encontrado em {filename}")

cap = cv2.VideoCapture(0)

print("\nIniciando reconhecimento... (pressione 'q' para sair)")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
   
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)
        name = "Desconhecido"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        top, right, bottom, left = face_location
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Reconhecimento Facial", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
