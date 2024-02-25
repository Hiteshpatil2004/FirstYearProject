import cv2

cap cv2.VideoCapture("https://192.168.172.85:8080/video")

while True:

ret, frame cap.read() # read from/image one by one resized cv2.resize(frame, (800,500)) cv2.imshow("Frame", resized) display frame/image

key = cv2.waitKey(1) #wait till key press

if key ord("Q"): sexit loop on 'q key press

break

cap.release() release video capture object

cv2.destroyAllWindows() #destroy all frame windowns
