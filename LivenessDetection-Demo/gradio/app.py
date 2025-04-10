import sys
sys.path.append('../')

import os
import gradio as gr
import cv2
import time
import numpy as np
from PIL import Image

from engine.header import get_version
from engine.header import get_deviceid
from engine.header import init_sdk
from engine.header import init_sdk_offline

from engine.header import check_liveness
from engine.header import print_log, print_error, print_info, print_warning

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
root_path = os.path.dirname(dir_path)

version = get_version().decode('utf-8')
print_info('\t <Recognito Liveness> \t version {}'.format(version))

device_id = get_deviceid().decode('utf-8')
print_info('\t <Hardware ID> \t\t {}'.format(device_id))

g_activation_result = -1
SPOOF_THRESHOLD = 0.5

css = """
.example-image img{
    display: flex; /* Use flexbox to align items */
    justify-content: center; /* Center the image horizontally */
    align-items: center; /* Center the image vertically */
    height: 300px; /* Set the height of the container */
    object-fit: contain; /* Preserve aspect ratio while fitting the image within the container */
}

.example-image{
    display: flex; /* Use flexbox to align items */
    justify-content: center; /* Center the image horizontally */
    align-items: center; /* Center the image vertically */
    height: 350px; /* Set the height of the container */
    object-fit: contain; /* Preserve aspect ratio while fitting the image within the container */
}

.face-row {
    display: flex;
    justify-content: space-around; /* Distribute space evenly between elements */
    align-items: center; /* Align items vertically */
    width: 100%; /* Set the width of the row to 100% */
}

.face-image{
    justify-content: center; /* Center the image horizontally */
    align-items: center; /* Center the image vertically */
    height: 160px; /* Set the height of the container */
    width: 160px;
    object-fit: contain; /* Preserve aspect ratio while fitting the image within the container */
}

.face-image img{
    justify-content: center; /* Center the image horizontally */
    align-items: center; /* Center the image vertically */
    height: 160px; /* Set the height of the container */
    object-fit: contain; /* Preserve aspect ratio while fitting the image within the container */
}

.markdown-success-container {
    background-color: #F6FFED;
    padding: 20px;
    margin: 20px;
    border-radius: 1px;
    border: 2px solid green;
    text-align: center;
}

.markdown-fail-container {
    background-color: #FFF1F0;
    padding: 20px;
    margin: 20px;
    border-radius: 1px;
    border: 2px solid red;
    text-align: center;
}

.markdown-attribute-container {
    display: flex;
    justify-content: space-around; /* Distribute space evenly between elements */
    align-items: center; /* Align items vertically */
    padding: 10px;
    margin: 10px;
}

.block-background {
    # background-color: #202020; /* Set your desired background color */
    border-radius: 5px;
}

table, th, td {
    text-align: center;    
}
"""


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

def convert_fun(input_str):
    # Remove line breaks and extra whitespaces
    return ' '.join(input_str.split())

def check_liveness_clicked(frame, threshold):   
    global g_activation_result
    if g_activation_result != 0:
        gr.Warning("SDK Activation Failed!")
        return None, None, None, None

    try:
        image = open(frame, 'rb')
    except:
        raise gr.Error("Please select image file!")
    
    image_mat = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    start_time = time.time()
    result, face_rect, score, angles = check_liveness(image_mat, float(threshold))
    end_time = time.time()
    process_time = (end_time - start_time) * 1000

    face_crop, one_line_attribute = None, ""
    try:
        image = Image.open(frame)

        face = Image.new('RGBA',(150, 150), (80,80,80,0))
        
        if face_rect is not None:
            x1 = int(face_rect[0])
            y1 = int(face_rect[1])
            x2 = int(face_rect[2])
            y2 = int(face_rect[3])

            if x1 < 0:
                x1 = 0
            if y1 < 0:
                y1 = 0
            if x2 >= image.width:
                x2 = image.width - 1
            if y2 >= image.height:
                y2 = image.height - 1

            if (x2 - x1) != 0 and (y2 - y1) != 0:    
                face_crop = image.crop((x1, y1, x2, y2))
                face_image_ratio = face_crop.width / float(face_crop.height)
                resized_w = int(face_image_ratio * 150)
                resized_h = 150

                face_crop = face_crop.resize((int(resized_w), int(resized_h)))

        if angles is not None:
            yaw = angles[0]
            roll = angles[1]
            pitch = angles[2]

        attribute = f"""
        <br/>
        <div class="markdown-attribute-container">
        <table>
        <tr>
            <th>Field</th>
            <th colspan="2">Value</th>
        </tr>
        <tr>
            <th rowspan="4">Face Rect</th>
            <td>x</td>
            <td>{x1}</td>
        </tr>
        <tr>
            <td>y</td>
            <td>{y1}</td>
        </tr>
        <tr>
            <td>width</td>
            <td>{x2 - x1 + 1}</td>
        </tr>
        <tr>
            <td>height</td>
            <td>{y2 - y1 + 1}</td>
        </tr>
        <tr>
            <th rowspan="3">Face Angle</th>
            <td>Pitch</td>
            <td>{"{:.4f}".format(pitch)}</td>
        </tr>
        <tr>
            <td>Yaw</td>
            <td>{"{:.4f}".format(yaw)}</td>
        </tr>
        <tr>
            <td>Roll</td>
            <td>{"{:.4f}".format(roll)}</td>
        </tr>
        </table>
        </div>
        """
        
        one_line_attribute = convert_fun(attribute)
    except:
        pass

    str_score = str("{:.4f}".format(score))
    if result == "REAL":
        liveness_result = f"""<br/><div class="markdown-success-container"><p style="text-align: center; font-size: 20px; color: green;">Liveness Check:  REAL<br/>Score: {str_score}</p></div>"""        
    else:
        liveness_result = f"""<br/><div class="markdown-fail-container"><p style="text-align: center; font-size: 20px; color: red;">Liveness Check:  {result}<br/>Score: {str_score}</p></div>"""  
        
    return face_crop, liveness_result, one_line_attribute, process_time

def launch_demo(activate_result):
    with gr.Blocks(css=css) as demo:
        gr.Markdown(
            f"""
            <a href="https://recognito.vision" style="display: flex; align-items: center;">
                <img src="https://recognito.vision/wp-content/uploads/2024/03/Recognito-modified.png" style="width: 3%; margin-right: 15px;"/>
            </a>
            <div style="display: flex; align-items: center;justify-content: center;">
                <p style="font-size: 36px; font-weight: bold;">Face Liveness Detection {version}</p>
            </div>
            <p style="font-size: 20px; font-weight: bold;">🤝 Contact us for our on-premise Face Recognition, Liveness Detection SDKs deployment</p>
            </div>
            <div style="display: flex; align-items: center;">
                &emsp;&emsp;<a target="_blank" href="mailto:hello@recognito.vision"><img src="https://img.shields.io/badge/email-hello@recognito.vision-blue.svg?logo=gmail " alt="www.recognito.vision"></a>
                &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://wa.me/+14158003112"><img src="https://img.shields.io/badge/whatsapp-recognito-blue.svg?logo=whatsapp " alt="www.recognito.vision"></a>
                &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://t.me/recognito_vision"><img src="https://img.shields.io/badge/telegram-@recognito-blue.svg?logo=telegram " alt="www.recognito.vision"></a>
                &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://join.slack.com/t/recognito-workspace/shared_invite/zt-2d4kscqgn-"><img src="https://img.shields.io/badge/slack-recognito-blue.svg?logo=slack " alt="www.recognito.vision"></a>
            </div>
            <br/>
            <div style="display: flex; align-items: center;">
                &emsp;&emsp;<a href="https://recognito.vision" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/recognito_64.png" style="width: 24px; margin-right: 5px;"/></a>
                &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.linkedin.com/company/recognito-vision" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/linkedin64.png" style="width: 24px; margin-right: 5px;"/></a>
                &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://huggingface.co/Recognito" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/hf1_64.png" style="width: 24px; margin-right: 5px;"/></a>
                &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/Recognito-Vision" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/github64.png" style="width: 24px; margin-right: 5px;"/></a>
                &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://hub.docker.com/u/recognito" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/docker64.png" style="width: 24px; margin-right: 5px;"/></a>
            </div>
            <br/>
            """
        )
    
                
        with gr.Group():
            if activate_result == 0:
                gr.Markdown("""<p style="text-align: left; font-size: 20px; color: green;">&emsp;Activation Success!</p>""")         
            else:
                gr.Markdown("""<p style="text-align: left; font-size: 20px; color: red;">&emsp;Activation Failed!</p>""") 
                    
            gr.Textbox(device_id, label="Hardware ID")
            

        with gr.Row():
            with gr.Column(scale=1):
                face_input = gr.Image(label="Image", type='filepath', elem_classes="example-image")
                gr.Examples([os.path.join(root_path,'examples/att_1.jpg'), 
                                    os.path.join(root_path,'examples/att_2.jpg'), 
                                    os.path.join(root_path,'examples/att_3.jpg'), 
                                    os.path.join(root_path,'examples/att_4.jpg'), 
                                    os.path.join(root_path,'examples/att_5.jpg'), 
                                    os.path.join(root_path,'examples/att_6.jpg'),  
                                    os.path.join(root_path,'examples/att_7.jpg')], 
                                    inputs=face_input)

            with gr.Blocks():
                with gr.Column(scale=1, elem_classes="block-background"):     
                    txt_threshold = gr.Textbox(f"{SPOOF_THRESHOLD}", label="Spoof Threshold", interactive=True)
                    check_liveness_button = gr.Button("Check Liveness", variant="primary", size="lg")
                    with gr.Row(elem_classes="face-row"):
                        face_output = gr.Image(value=os.path.join(dir_path,'icons/face.jpg'), label="Face", scale=0, elem_classes="face-image")
                    
                    liveness_result = gr.Markdown("")
                    txt_speed = gr.Textbox(f"", label="Processing Time (ms)", interactive=False, visible=False)
                    attribute_result = gr.Markdown("")
                
                check_liveness_button.click(check_liveness_clicked, inputs=[face_input, txt_threshold], outputs=[face_output, liveness_result, attribute_result, txt_speed])

    demo.launch(server_name="0.0.0.0", server_port=7860, show_api=False)
    
if __name__ == '__main__':
    g_activation_result = activate_sdk()
    launch_demo(g_activation_result)
