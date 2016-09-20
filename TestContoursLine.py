import cv2 
import numpy as np

def nothing(x):
    pass

im = cv2.imread('baboon.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('frame',im)

cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
cv2.createTrackbar("Hx", 'frame',0,255,nothing)
cv2.createTrackbar("Hn", 'frame',0,255,nothing)
cv2.createTrackbar("Sx", 'frame',0,255,nothing)
cv2.createTrackbar("Sn", 'frame',0,255,nothing)
cv2.createTrackbar("Vx", 'frame',0,255,nothing)
cv2.createTrackbar("Vn", 'frame',0,255,nothing)
while():  
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    hx = cv2.getTrackbarPos("Hx",'frame')
    hn = cv2.getTrackbarPos("Hn",'frame')
    sx = cv2.getTrackbarPos("Sx",'frame')
    sn = cv2.getTrackbarPos("Sn",'frame')
    vx = cv2.getTrackbarPos("Vx",'frame')
    vn = cv2.getTrackbarPos("Vn",'frame')
    
    lower_blue = np.array([hn, sn, vn])
    upper_blue = np.array([hx, sx, vx])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(im,im, mask= mask)
    
    cv2.imshow('frame',im)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    if  cv2.waitKey(1) & 0xFF == ord('q') :
        break

    
cv2.waitKey(0)
cv2.destroyAllWindows()
    
