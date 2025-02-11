import cv2
import os
# Opens the laptop camera (as 0 is the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break

    cv2.imshow('Video Feed', frame)
    img_counter=0

    # Pressing 'q' on the keyboard will exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Pressing 's' on the keyboard will capture a new image
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        im=f"captured_image_{img_counter}.png"
        path=os.path.join("C:/Users/mayan/Desktop",im)
        cv2.imwrite(im,frame)
        print("captured")
        
        img_counter=img_counter+1

cap.release()
cv2.destroyAllWindows()
