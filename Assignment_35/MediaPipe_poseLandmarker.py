import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
  
    while True:
      _ , frame = cap.read()

      frame.flags.writeable = False
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      results = pose.process(frame)

      # Draw pose 
      frame.flags.writeable = True
      frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
      mp_drawing.draw_landmarks(frame,results.pose_landmarks, mp_pose.POSE_CONNECTIONS, landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
      
      
      cv2.imshow('MediaPipe Pose', cv2.flip(frame, 1))
      if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()