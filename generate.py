import cv2
import time
import numpy as np


cap = cv2.VideoCapture("cut.mp4")

# We give some time for the camera to setup
time.sleep(3)

# Automatically grab width and height from video feed
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'XVID'),1, (width, height))
frames=[]
i=0
while(cap.isOpened()):
    
    ret, img = cap.read()
    
    if not ret:
        break
    
    frames.append(img)
    
    #Calculating the median of 54 frames and writing their median to a file 
    if len(frames)==54:
        medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
        if i==0:
            cv2.imwrite('street.jpg',medianFrame)
            i+=1
        writer.write(medianFrame)
        frames=[]
        
    
    
    #cv2.imshow('Magic !!!',img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
writer.write(medianFrame)


cap.release()
writer.release()
cv2.destroyAllWindows()
print("Writing Done!!")
