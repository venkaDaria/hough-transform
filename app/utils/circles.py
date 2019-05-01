import cv2
import numpy as np

def hough_image(img, max_slider):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cimg = np.copy(img)

    p1 = max_slider
    p2 = max_slider * 0.4

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, cimg.shape[0]/64, param1=p1, param2=p2, minRadius=25, maxRadius=50)
    
    if circles is not None:
        cir_len = circles.shape[1]
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    return cimg

def hough_images(images, max_slider):
    return [hough_image(img, max_slider) for img in images]
