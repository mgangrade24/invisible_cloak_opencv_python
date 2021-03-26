import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read() #take each frame
    
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv", hsv)
        #how to get hsv value?
        #lower:hue-10,100,100  higher:h+10,255,255
        red = np.uint8([[[255,0,0]]]) #bgr value of red
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        #get hsv value of red from bgr
        #print(hsv_red)
        
        #threshold the hsv value to get only red colors
        l_red = np.array([110,100,100])
        u_red = np.array([130,255,255])
        
        mask = cv2.inRange(hsv, l_red, u_red)
        #cv2.imshow("mask", mask)
        
        part1 = cv2.bitwise_and(back, back, mask=mask) #all things red
        #cv2.imshow("part1", part1)
        
        mask = cv2.bitwise_not(mask)
        
        part2 = cv2.bitwise_and(frame, frame, mask=mask) #all things not red
        #cv2.imshow("mask", part2)
        
        cv2.imshow("cloak", part1+part2)
        
        
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()