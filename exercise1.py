
import cv2
import numpy as np
import os


image = cv2.imread('image.png')
blu,green,redd = cv2.split(image)


b = cv2.mean(blu)
r = cv2.mean(redd)
g = cv2.mean(green)

cv2.putText(blu,b.__str__(),(50 , 50),  cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),2, lineType=cv2.LINE_AA)
cv2.putText(redd,r.__str__(),(50 , 50),  cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),2, lineType=cv2.LINE_AA)
cv2.putText(green,g.__str__(),(50 , 50),  cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),2, lineType=cv2.LINE_AA)
cv2.imshow('R-RGB', redd)
cv2.imshow('B-RGB', blu)
cv2.imshow('G-RGB', green)


cv2.waitKey(0)