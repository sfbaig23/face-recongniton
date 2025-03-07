import cv2

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open webcam (Ensure it's properly opened)
video_cap = cv2.VideoCapture(0)
if not video_cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    ret, frame = video_cap.read()
    
    if not ret:
        print("Error: Failed to capture frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6, minSize=(30, 30))

    # Draw rectangles around multiple detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Multi-Face Detection & Tracking", frame)  # Show video with face tracking

    if cv2.waitKey(1) & 0xFF == ord("f"):  # Press 'f' to exit
        break

# Release resources
video_cap.release()
cv2.destroyAllWindows()
