import cv2
import mediapipe as mp
from playsound import playsound
import threading

def main():
    camera_id = 0
    
    cap = cv2.VideoCapture(camera_id)
    
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    
    if not cap.isOpened():
        print("Camera didn't open!")
        return
    
    threading.Thread(target=start_camera, args=(cap, hands)).start()

def start_camera(cap, hands):
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
               playsound("notification.mp3")
                    
    
    cap.release()

if __name__ == '__main__':
    main()
