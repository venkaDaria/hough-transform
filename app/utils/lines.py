import cv2
import numpy as np

def hough_image(img, max_slider):
    dst = np.copy(img)
    
    th1 = max_slider 
    th2 = max_slider * 0.4

    edges = cv2.Canny(img, th1, th2)
    
    lines = cv2.HoughLinesP(edges, 2, np.pi/180.0, 50, minLineLength=10, maxLineGap=100)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(dst, (x1, y1), (x2, y2), (0,0,255), 1)

    return dst
    
def hough_images(images, max_slider):
    return [hough_image(img, max_slider) for img in images]
