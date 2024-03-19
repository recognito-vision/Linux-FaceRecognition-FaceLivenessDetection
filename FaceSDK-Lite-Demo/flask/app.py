import sys
sys.path.append('../')

import os
import base64
import json
import cv2
import uuid
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve
from time import gmtime, strftime

from engine.header import *

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
root_path = os.path.dirname(dir_path)

MATCH_THRESHOLD = 0.82

app = Flask(__name__)
CORS(app)

print_info('\t Recognito Face SDK Lite version')

def activate_sdk():
    key_path = os.path.join(root_path, "license.txt")
    
    ret = -1
    if os.path.exists(key_path) is False:
        print_warning("License key file not found!")
        print_error(f"Falied to init SDK, Error code {ret}")
        return ret
    else:
        ret = init_sdk(key_path.encode('utf-8'))
        if ret == 0:
            print_log("Successfully init SDK!")
        else:
            print_error(f"Falied to init SDK, Error code {ret}")
            return ret

    return ret

@app.route('/api/analyze_face', methods=['POST'])
def analyze_face_api():
    status = "ok"
    data = {
        "status": status, 
        "data": {}
    }

    try:
        file = request.files['image']
        image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    except:
        data["data"]["result"] = "Failed to open image"   
        response = jsonify(data)
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    ret, face_rect, attribute, template = detect_face(image)
    if ret != 0:
        if ret == ENGINE_CODE.E_ENGINE_INIT_ERROR.value:
            result = "ENGINE INIT ERROR"
        elif ret == ENGINE_CODE.E_NO_FACE.value:
            result = "NO FACE"
        else:
            result = "ENGINE ERROR"

        data["data"]["result"] = result   
        response = jsonify(data)
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
    
    data["data"]["result"] = "FACE DETECTED"

    if face_rect is not None:
        data["data"]["face_rect"] = {
            "x": int(face_rect[0]), 
            "y": int(face_rect[1]), 
            "w": int(face_rect[2] - face_rect[0] + 1), 
            "h": int(face_rect[3] - face_rect[1] + 1)
        }
    
    if attribute is not None:
        attr = {}
        if attribute.liveness == LIVENESS_CODE.L_SPOOF.value:
            liveness = "SPOOF"
        elif attribute.liveness == LIVENESS_CODE.L_REAL.value:
            liveness = "REAL"
        elif attribute.liveness == LIVENESS_CODE.L_TOO_SMALL_FACE.value:    
            liveness = "TOO SMALL FACE"
        elif attribute.liveness == LIVENESS_CODE.L_TOO_LARGE_FACE.value:
            liveness = "TOO LARGE FACE"
        elif attribute.liveness == LIVENESS_CODE.L_NO_FACE.value:
            liveness = "NO FACE"
        elif attribute.liveness == LIVENESS_CODE.L_LIVENESS_CHECK_FAILED.value:
            liveness = "Liveness Check Failed"
        else:    
            liveness = "ERROR"

        attr["liveness"] = liveness
        attr["gender"] = "MALE" if attribute.gender == 0 else "FEMALE"
        attr["age"] = str(attribute.age)
        attr["angle"] = {"roll": str(attribute.angle[0]),
                          "yaw": str(attribute.angle[1]),
                          "pitch": str(attribute.angle[2])}
        attr["eye_open"] = {"left_eye": "OPEN" if attribute.eye_open[0] == 1 else "CLOSE",
                            "right_eye": "OPEN" if attribute.eye_open[1] == 1 else "CLOSE"}
        attr["wear_glass"] = "YES" if attribute.wear_glass == 1 else "NO"
        attr["mouth_open"] = "YES" if attribute.mouth_close == 0 else "NO"
        attr["mask"] = "YES" if attribute.mask == 1 else "NO"
        data["data"]["attribute"] = attr

    # if template is not None:
    #     templeate_str = json.dumps(template.tolist(), indent=0).replace('\n','')
    #     data["data"]["feature"] = templeate_str

    response = jsonify(data)
    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.route('/api/compare_face', methods=['POST'])
def compare_face_api():
    status = "ok"
    data = {
        "status": status, 
        "data": {}
    }

    try:
        file1 = request.files['image1']
        image1 = cv2.imdecode(np.frombuffer(file1.read(), np.uint8), cv2.IMREAD_COLOR)
    except:
        data["data"]["result"] = "Failed to open image1"   
        response = jsonify(data)
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    try:
        file2 = request.files['image2']
        image2 = cv2.imdecode(np.frombuffer(file2.read(), np.uint8), cv2.IMREAD_COLOR)
    except:
        data["data"]["result"] = "Failed to open image2"   
        response = jsonify(data)
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    ret, face_rect1, _, template1 = detect_face(image1)
    if ret != 0:
        if ret == ENGINE_CODE.E_ENGINE_INIT_ERROR.value:
            result = "ENGINE INIT ERROR"
        elif ret == ENGINE_CODE.E_NO_FACE.value:
            result = "NO FACE in image1"
        else:
            result = "ENGINE ERROR"

        data["data"]["result"] = result   
        response = jsonify(data)
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    ret, face_rect2, _, template2 = detect_face(image2)
    if ret != 0:
        if ret == ENGINE_CODE.E_ENGINE_INIT_ERROR.value:
            result = "ENGINE INIT ERROR"
        elif ret == ENGINE_CODE.E_NO_FACE.value:
            result = "NO FACE in image2"
        else:
            result = "ENGINE ERROR"

        data["data"]["result"] = result   
        response = jsonify(data)
        response.status_code = 200
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response

    detection = {}
    if face_rect1 is not None:
        detection["face1"] = {
            "x" : int(face_rect1[0]),
            "y" : int(face_rect1[1]),
            "width" : int(face_rect1[2] - face_rect1[0] + 1),
            "height" : int(face_rect1[3] - face_rect1[1] + 1)
        }

    if face_rect2 is not None:
        detection["face2"] = {
            "x" : int(face_rect2[0]),
            "y" : int(face_rect2[1]),
            "width" : int(face_rect2[2] - face_rect2[0] + 1),
            "height" : int(face_rect2[3] - face_rect2[1] + 1)
        }
    data["data"]["detection"] = detection   

    similarity = get_similarity(template1, template2)
    if similarity > MATCH_THRESHOLD:
        result = "SAME PERSON"
    else:
        result = "DIFFERENT PERSON"
    
    data["data"]["result"] = result   
    data["data"]["similarity"] = float(similarity)
    response = jsonify(data)
    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

if __name__ == '__main__':
    ret = activate_sdk()
    if ret != 0:
        exit(-1)

    serve(app, host='0.0.0.0', port=8000)