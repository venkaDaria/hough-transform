from flask import Flask, render_template, request, redirect, url_for

from utils.funcs import read_image, save_image, to_base64, from_base64, from_base64_simple

import utils.circles as circles
import utils.lines as lines
import utils.edges as edges

import json
import os
import datetime

app = Flask(__name__)
datasets = "./datasets/"
result = "./result/"

transform_modules = {
    "lines": lines,
    "circles": circles,
    "edges": edges
}

# UTILS
def get_directories(root):
    return [name for name in os.listdir(root) if os.path.isdir(root + name)]

def get_images(path):
    files = os.listdir(path)
    return [read_image(path + f) for f in files]

def map_images(images):
    return [from_base64_simple(img) for img in images]

def save_images(root, data): 
    folder = root + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + "/"
    if not os.path.exists(folder):
        os.makedirs(folder)
    for index, img in enumerate(data):
        save_image(from_base64(img), folder + str(index))

# HOUGH TRANSFORM  
def hough(request):
    transform_type = request.form['type']
    transform_module = transform_modules[transform_type]
    
    images_data = request.form.getlist('images_data')
    if len(images_data) > 0:
        images = map_images(images_data)
    else:    
        dataset_name = request.form['dataset']
        images = get_images(datasets + dataset_name + "/")

    threshold = float(request.form['threshold'])

    transformed = transform_module.hough_images(images, threshold)
    return render_template(
        'index.html', 
        dirs=get_directories(datasets),
        dataset=[to_base64(im) for im in images],
        result=[to_base64(im) for im in transformed]
    )

# GET PAGE
@app.route('/',  methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        return hough(request)   
    return render_template('index.html', dirs=get_directories(datasets), dataset=[], result=[])

# API UTILS
@app.route('/api/save',  methods=['POST'])
def save():
    save_images(result, request.form.getlist('data[]'))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/api/clear',  methods=['POST'])
def clear():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
  
# RUN    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
