import cv2 
import  numpy as np
def detect_yellow():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Define the range for yellow color in HSV
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])
        
        # Create a mask for yellow color
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                print(f"Detected yellow object at x={x}, y={y}, w={w}, h={h}")
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
        # Display the resulting frame
        cv2.imshow('Yellow Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_yellow()
