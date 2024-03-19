import sys
sys.path.append('../')

import os
import base64
import json
import cv2
import numpy as np
from flask import Flask, request, jsonify
from time import gmtime, strftime

from engine.header import *

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
root_path = os.path.dirname(dir_path)

MATCH_THRESHOLD = 0.67

app = Flask(__name__) 
app.config['SITE'] = "http://0.0.0.0:8000/"
app.config['DEBUG'] = False

version = get_version().decode('utf-8')
print_info('\t <Recognito Face Recognition> \t version {}'.format(version))

device_id = get_deviceid().decode('utf-8')
print_info('\t <Hardware ID> \t\t {}'.format(device_id))

def activate_sdk():
    online_key = os.environ.get("FR_LICENSE_KEY")
    offline_key_path = os.path.join(root_path, "license.txt")
    dict_path = os.path.join(root_path, "engine/bin")

    ret = -1
    if online_key is None:
        print_warning("Recognition online license key not found!")
    else:
        print_info(f"FR_LICENSE_KEY: {online_key}")
        ret = init_sdk(dict_path.encode('utf-8'), online_key.encode('utf-8'))

    if ret == 0:
        print_log("Successfully online init SDK!")
    else:
        print_error(f"Failed to online init SDK, Error code {ret}\n Trying offline init SDK...");
        if os.path.exists(offline_key_path) is False:
            print_warning("Recognition offline license key file not found!")
            print_error(f"Falied to offline init SDK, Error code {ret}")
            return ret
        else:
            ret = init_sdk_offline(dict_path.encode('utf-8'), offline_key_path.encode('utf-8'))
            if ret == 0:
                print_log("Successfully offline init SDK!")
            else:
                print_error(f"Falied to offline init SDK, Error code {ret}")
                return ret
                
    return ret

def generate_response(result, similarity=None, face_bboxes=None, face_features=None):
    status = "ok"
    data = {
        "status": status, 
        "data": {}
    }
    
    data["data"]["result"] = result    
    if similarity is not None:
        data["data"]["similarity"] = float(similarity)    
    images = [{}, {}]
    if face_bboxes is not None:
        for i, bbox in enumerate(face_bboxes):
            box = {
                "x" : int(bbox[0]),
                "y" : int(bbox[1]),
                "width" : int(bbox[2] - bbox[0] + 1),
                "height" : int(bbox[3] - bbox[1] + 1)
            }
            images[i]["detection"] = box
        
    if face_features is not None:
        for i, feat in enumerate(face_features):
            json_string = json.dumps(feat.tolist(), indent=0).replace('\n','')
            images[i]["feature"] = json_string
            
    data["data"]["image1"] = images[0]
    data["data"]["image2"] = images[1]

    response = jsonify(data)
    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response
    
@app.route('/api/compare_face', methods=['POST'])
def compare_face_api():
    try:
        file1 = request.files['image1']
        image_mat1 = cv2.imdecode(np.frombuffer(file1.read(), np.uint8), cv2.IMREAD_COLOR)
    except:
        response = generate_response("Failed to open image1")
        return response

    try:
        file2 = request.files['image2']
        image_mat2 = cv2.imdecode(np.frombuffer(file2.read(), np.uint8), cv2.IMREAD_COLOR)
    except:
        response = generate_response("Failed to open image2")
        return response        

    result, score, face_bboxes, face_features = compare_face(image_mat1, image_mat2, MATCH_THRESHOLD)
    response = generate_response(result, score, face_bboxes, face_features)
    return response


@app.route('/api/compare_face_base64', methods=['POST'])
def coompare_face_base64_api():
    content = request.get_json()
    
    try:
        image_base64_1 = content['image1']
        image_mat1 = cv2.imdecode(np.frombuffer(base64.b64decode(image_base64_1), dtype=np.uint8), cv2.IMREAD_COLOR)
    except:
        response = generate_response("Failed to open image1")
        return response

    try:
        image_base64_2 = content['image2']
        image_mat2 = cv2.imdecode(np.frombuffer(base64.b64decode(image_base64_2), dtype=np.uint8), cv2.IMREAD_COLOR)
    except:
        response = generate_response("Failed to open image2")
        return response

    result, score, face_bboxes, face_features = compare_face(image_mat1, image_mat2, MATCH_THRESHOLD)
    response = generate_response(result, score, face_bboxes, face_features)
    return response

if __name__ == '__main__':
    ret = activate_sdk()
    if ret != 0:
        exit(-1)
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
