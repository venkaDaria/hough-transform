import cv2
import numpy as np
import base64
import re
import matplotlib.pyplot as plt 

uri_start = "data:image/jpeg;base64,"

def read_image(filename):
    return cv2.imread(filename)

def save_image(img, fname):
    plt.imsave(fname, img.astype(np.uint8))

def to_base64(img):
    retval, buffer = cv2.imencode('.jpg', img)
    return uri_start + base64.b64encode(buffer).decode("utf-8")

def from_base64(uri):
    imageBGR = from_base64_simple(uri)
    imageRGB = cv2.cvtColor(imageBGR , cv2.COLOR_BGR2RGB)
    return imageRGB

def from_base64_simple(uri):
    byts = re.sub(uri_start, '', uri)
    nparr = np.frombuffer(base64.b64decode(byts), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    