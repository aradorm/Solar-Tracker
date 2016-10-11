import cv2
import numpy as np

cv2.namedWindow("original")
cv2.namedWindow("filltered")
cam = cv2.VideoCapture(0)

if cam.isOpened(): # try to get the first frame
    rval, a = cam.read()
else:
    rval = False

TRGTx = int(cam.get(3)/2)
TRGTy = int(cam.get(4)/2)

xInteg = 0
yInteg = 0
dt = 0.02
    
Kp = 0.001
Ki = 0.001

while rval:
    rval, a = cam.read()
    b = a
    b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    b = cv2.GaussianBlur(b,(5,5),0)
    th, b = cv2.threshold(b,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = np.ones((5,5),np.uint8)
    b = cv2.morphologyEx(b, cv2.MORPH_OPEN, kernel)
    #calculating the center of area
    M = cv2.moments(b)
    CGx = int(M['m10']/M['m00'])
    CGy = int(M['m01']/M['m00'])
    #marking the center of area and target
    cv2.circle(a,(CGx,CGy),6,(0,0,255),-1)
    cv2.circle(a,(TRGTx,TRGTy),6,(0,255,0),-1)
    #generating error term
    ERRx = CGx-TRGTx
    ERRy = CGy-TRGTy
    
    #display preview
    cv2.imshow("original", a)
    cv2.imshow("filltered", b)
    
    # PID controller
    xSignal = Kp*ERRx+Ki*xInteg
    ySignal = Kp*ERRy+Ki*yInteg
    print(xSignal, ySignal)
    xInteg = xInteg+ERRx*dt
    yInteg = yInteg+ERRy*dt
    #terminating program
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("original")
cv2.destroyWindow("filltered")