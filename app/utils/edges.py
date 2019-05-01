import cv2

def edges(img, max_slider):
    return cv2.Canny(img, max_slider, max_slider * 0.4)
    
def hough_images(images, max_slider):
    return [edges(img, max_slider) for img in images]
