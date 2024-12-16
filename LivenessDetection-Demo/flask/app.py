import sys
sys.path.append('../')

import os
import base64
import json
import cv2
import numpy as np
from time import gmtime, strftime
from flask import Flask, request, jsonify

from engine.header import get_version
from engine.header import get_deviceid
from engine.header import init_sdk
from engine.header import init_sdk_offline

from engine.header import check_liveness
from engine.header import print_log, print_error, print_info, print_warning

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
root_path = os.path.dirname(dir_path)

SPOOF_THRESHOLD = 0.5

app = Flask(__name__) 
app.config['SITE'] = "http://0.0.0.0:8000/"
app.config['DEBUG'] = False

version = get_version().decode('utf-8')
print_info('\t <Recognito Liveness> \t version {}'.format(version))

device_id = get_deviceid().decode('utf-8')
print_info('\t <Hardware ID> \t\t {}'.format(device_id))

def activate_sdk():
    online_key = os.environ.get("FL_LICENSE_KEY")
    offline_key_path = os.path.join(root_path, "license.txt")
    dict_path = os.path.join(root_path, "engine/bin")

    ret = -1
    if online_key is None:
        print_warning("Liveness online license key not found!")
    else:
        print_info(f"FL_LICENSE_KEY: {online_key}")
        ret = init_sdk(dict_path.encode('utf-8'), online_key.encode('utf-8'))

    if ret == 0:
        print_log("Successfully online init SDK!")
    else:
        print_error(f"Failed to online init SDK, Error code {ret}\n Trying offline init SDK...");
        if os.path.exists(offline_key_path) is False:
            print_warning("Liveness offline license key file not found!")
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

def generate_response(result, face_rect, score, angles):
    status = "ok"
    data = {
        "status": status, 
        "data": {}
    }

    data["data"]["result"] = result    

    if score is not None:
        data["data"]["liveness_score"] = score

    if face_rect is not None:
        data["data"]["face_rect"] = {
            "x": int(face_rect[0]), 
            "y": int(face_rect[1]), 
            "w": int(face_rect[2] - face_rect[0] + 1), 
            "h": int(face_rect[3] - face_rect[1] + 1)
        }

    if angles is not None:
        data["data"]["angles"] = {
            "yaw": angles[0], 
            "roll": angles[1], 
            "pitch": angles[2]
        }

    response = jsonify(data)
    response.status_code = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response
    
@app.route('/api/check_liveness', methods=['POST'])
def check_liveness_api():
    try:
        file = request.files['image']
        image_mat = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    except:
        response = generate_response("Failed to open file!", None, None, None)
        return response
    
    result, face_rect, score, angles = check_liveness(image_mat, SPOOF_THRESHOLD)
    response = generate_response(result, face_rect, score, angles)
    return response

@app.route('/api/check_liveness_base64', methods=['POST'])
def check_liveness_base64_api():
    try: 
        content = request.get_json()
        imageBase64 = content['image']
        image_mat = cv2.imdecode(np.frombuffer(base64.b64decode(imageBase64), dtype=np.uint8), cv2.IMREAD_COLOR)
    except:
        response = generate_response("Failed to open file!", None, None, None)
        return response
    
    result, face_rect, score, angles = check_liveness(image_mat, SPOOF_THRESHOLD)
    response = generate_response(result, face_rect, score, angles)
    return response

if __name__ == '__main__':
    ret = activate_sdk()
    if ret != 0:
        exit(-1)
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
