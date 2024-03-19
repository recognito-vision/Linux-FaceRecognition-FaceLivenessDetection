import sys
sys.path.append('../')

import os
import gradio as gr
import cv2
import time
import numpy as np
from PIL import Image

from engine.header import *

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
root_path = os.path.dirname(dir_path)

print_info('\t Recognito Face SDK Lite version')

g_activation_result = -1
MATCH_THRESHOLD = 0.82

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

"""


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

def convert_fun(input_str):
    # Remove line breaks and extra whitespaces
    return ' '.join(input_str.split())

def analyze_face_clicked(frame):    
    global g_activation_result
    if g_activation_result != 0:
        gr.Warning("SDK Activation Failed!")
        return None, None, None

    try:
        image = open(frame, 'rb')
    except:
        raise gr.Error("Please select images file!")

    image_mat = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    start_time = time.time()
    ret, face_rect, attribute, template = detect_face(image_mat)
    end_time = time.time()
    process_time = (end_time - start_time) * 1000

    if ret != 0:
        if ret == ENGINE_CODE.E_ENGINE_INIT_ERROR.value:
            result = "ENGINE INIT ERROR"
        elif ret == ENGINE_CODE.E_NO_FACE.value:
            result = "NO FACE"
        else:
            result = "ENGINE ERROR"
        gr.Warning(result)
        return None, None, None

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

            face_crop = image.crop((x1, y1, x2, y2))
            face_image_ratio = face_crop.width / float(face_crop.height)
            resized_w = int(face_image_ratio * 150)
            resized_h = 150

            face_crop = face_crop.resize((int(resized_w), int(resized_h)))
            
        if attribute is not None:
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

            if liveness == 'REAL':
                liveness_result = f"""<br/><div class="markdown-success-container"><p style="text-align: center; font-size: 20px; color: green;">Liveness Check:  REAL<br/>Score: {attribute.liveness}</p></div>"""
            else:
                liveness_result = f"""<br/><div class="markdown-fail-container"><p style="text-align: center; font-size: 20px; color: red;">Liveness Check:  {liveness}<br/>Score: {attribute.liveness}</p></div>"""

            gender = "MALE" if attribute.gender == 0 else "FEMALE"
            age = attribute.age
            [roll, yaw, pitch] = attribute.angle
            left_eye = "OPEN" if attribute.eye_open[0] == 1 else "CLOSE"
            right_eye = "OPEN" if attribute.eye_open[1] == 1 else "CLOSE"
            wear_glass = "YES" if attribute.wear_glass == 1 else "NO"
            mouth_open = "YES" if attribute.mouth_close == 0 else "NO"
            mask = "YES" if attribute.mask == 1 else "NO"
            

            attribute = f"""
            <br/>
            <div class="markdown-attribute-container">
            <table>
            <tr>
                <th style="text-align: center;">Attribute</th>
                <th style="text-align: center;">Result</th>
            </tr>
            <tr>
                <td>Gender</td>
                <td>{gender}</td>
            </tr>
            <tr>
                <td>Age</td>
                <td>{int(age)}</td>
            </tr>
            <tr>
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
            <tr>
                <td>Left Eye</td>
                <td>{left_eye}</td>
            </tr>
            <tr>
                <td>Right Eye</td>
                <td>{right_eye}</td>
            </tr>
            <tr>
                <td>Mask</td>
                <td>{mask}</td>
            </tr>
            <tr>
                <td>Glass</td>
                <td>{wear_glass}</td>
            </tr>
            <tr>
                <td>Open Mouth</td>
                <td>{mouth_open}</td>
            </tr>
            </table>
            </div>
            """
            one_line_attribute = convert_fun(attribute)
    except:
        pass
    
    return face_crop, liveness_result, one_line_attribute

def compare_face_clicked(frame1, frame2, threshold):
    global g_activation_result
    if g_activation_result != 0:
        gr.Warning("SDK Activation Failed!")
        return None, None, None, None, None, None, None, None, None

    try:
        image1 = open(frame1, 'rb')
        image2 = open(frame2, 'rb')
    except:
        raise gr.Error("Please select images files!")

    image_mat1 = cv2.imdecode(np.frombuffer(image1.read(), np.uint8), cv2.IMREAD_COLOR)
    image_mat2 = cv2.imdecode(np.frombuffer(image2.read(), np.uint8), cv2.IMREAD_COLOR)
    start_time = time.time()
    ret1, face_rect1, attribute1, template1 = detect_face(image_mat1)
    if ret1 != 0:
        if ret1 == ENGINE_CODE.E_ENGINE_INIT_ERROR.value:
            gr.Warning("ENGINE INIT ERROR")
        elif ret1 == ENGINE_CODE.E_NO_FACE.value:
            gr.Warning("NO FACE in image1")
        else:
            gr.Warning("ENGINE ERROR")
        return None, None, None, None, None, None, None, None, None

    ret2, face_rect2, attribute2, template2 = detect_face(image_mat2)
    if ret2 != 0:
        if ret2 == ENGINE_CODE.E_ENGINE_INIT_ERROR.value:
            gr.Warning("ENGINE INIT ERROR")
        elif ret2 == ENGINE_CODE.E_NO_FACE.value:
            gr.Warning("NO FACE in image2")
        else:
            gr.Warning("ENGINE ERROR")
        return None, None, None, None, None, None, None, None, None

    similarity = get_similarity(template1, template2)
    end_time = time.time()
    process_time = (end_time - start_time) * 1000

    try:
        image1 = Image.open(frame1)
        image2 = Image.open(frame2)
        images = [image1, image2]

        face1 = Image.new('RGBA',(150, 150), (80,80,80,0))
        face2 = Image.new('RGBA',(150, 150), (80,80,80,0))
        faces = [face1, face2]
        
        face_bboxes = [face_rect1, face_rect2]
        face_bboxes_result = []
        for i, bbox in enumerate(face_bboxes):
            x1 = bbox[0]
            y1 = bbox[1]
            x2 = bbox[2]
            y2 = bbox[3]
            if x1 < 0:
                x1 = 0
            if y1 < 0:
                y1 = 0
            if x2 >= images[i].width:
                x2 = images[i].width - 1
            if y2 >= images[i].height:
                y2 = images[i].height - 1

            face_bbox_str = f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}"
            face_bboxes_result.append(face_bbox_str)

            faces[i] = images[i].crop((x1, y1, x2, y2))
            face_image_ratio = faces[i].width / float(faces[i].height)
            resized_w = int(face_image_ratio * 150)
            resized_h = 150

            faces[i] = faces[i].resize((int(resized_w), int(resized_h)))
    except:
        pass
        
    matching_result = Image.open(os.path.join(dir_path, "icons/blank.png"))
    similarity_score = ""
    if face1 is not None and face2 is not None:
        if similarity is not None:
            str_score = str("{:.4f}".format(similarity))
        
            if similarity >= float(threshold):
                matching_result = Image.open(os.path.join(dir_path, "icons/same.png"))
                similarity_score = f"""<br/><div class="markdown-success-container"><p style="text-align: center; font-size: 20px; color: green;">Similarity score: {str_score}</p></div>"""
            else:
                matching_result = Image.open(os.path.join(dir_path, "icons/different.png"))
                similarity_score = f"""<br/><div class="markdown-fail-container"><p style="text-align: center; font-size: 20px; color: red;">Similarity score: {str_score}</p></div>"""
    
    return faces[0], faces[1], matching_result, similarity_score, face_bboxes_result[0], face_bboxes_result[1], template1, template2, str(process_time)

def launch_demo(activate_result):
    with gr.Blocks(css=css) as demo:
        gr.Markdown(
            f"""
            <a href="https://recognito.vision" style="display: flex; align-items: center;">
                <img src="https://recognito.vision/wp-content/uploads/2024/03/Recognito-modified.png" style="width: 3%; margin-right: 15px;"/>
            </a>
            <div style="display: flex; align-items: center;justify-content: center;">
                <p style="font-size: 36px; font-weight: bold;">Face Recognition and Analysis - Lite Version</p>
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
                    
        with gr.Tabs():
            with gr.Tab("Face Recognition"):
                with gr.Row():
                    with gr.Column(scale=2):
                        with gr.Row():
                            with gr.Column(scale=1):
                                compare_face_input1 = gr.Image(label="Image1", type='filepath', elem_classes="example-image")
                                gr.Examples([os.path.join(root_path,'examples/1.jpg'), 
                                            os.path.join(root_path,'examples/2.jpg'), 
                                            os.path.join(root_path,'examples/3.jpg'), 
                                            os.path.join(root_path,'examples/4.jpg')], 
                                            inputs=compare_face_input1)
                            with gr.Column(scale=1):
                                compare_face_input2 = gr.Image(label="Image2", type='filepath', elem_classes="example-image")
                                gr.Examples([os.path.join(root_path,'examples/5.jpg'),
                                            os.path.join(root_path,'examples/6.jpg'),
                                            os.path.join(root_path,'examples/7.jpg'),
                                            os.path.join(root_path,'examples/8.jpg')],
                                            inputs=compare_face_input2)
                    with gr.Blocks():          
                        with gr.Column(scale=1, min_width=400, elem_classes="block-background"):     
                            txt_threshold = gr.Textbox(f"{MATCH_THRESHOLD}", label="Matching Threshold", interactive=True)
                            compare_face_button = gr.Button("Compare Face", variant="primary", size="lg")
                            with gr.Row(elem_classes="face-row"):
                                face_output1 = gr.Image(value=os.path.join(dir_path,'icons/face.jpg'), label="Face 1", scale=0, elem_classes="face-image")
                                compare_result = gr.Image(value=os.path.join(dir_path,'icons/blank.png'), min_width=30, scale=0, show_download_button=False, show_label=False)
                                face_output2 = gr.Image(value=os.path.join(dir_path,'icons/face.jpg'), label="Face 2", scale=0, elem_classes="face-image")
                            similarity_markdown = gr.Markdown("")
                            txt_speed = gr.Textbox(f"", label="Processing Time (ms)", interactive=False, visible=False)
                            with gr.Group():
                                gr.Markdown("""&nbsp;face1""")
                                txt_bbox1 = gr.Textbox(f"", label="Rect", interactive=False)
                                txt_feature1 = gr.Textbox(f"", label="Feature", interactive=False, max_lines=5)
                            with gr.Group():
                                gr.Markdown("""&nbsp;face2""")
                                txt_bbox2 = gr.Textbox(f"", label="Rect", interactive=False)
                                txt_feature2 = gr.Textbox(f"", label="Feature", interactive=False, max_lines=5)

                            compare_face_button.click(compare_face_clicked, inputs=[compare_face_input1, compare_face_input2, txt_threshold], outputs=[face_output1, face_output2, compare_result, similarity_markdown, txt_bbox1, txt_bbox2, txt_feature1, txt_feature2, txt_speed])
                    
            with gr.Tab("Face Liveness, Analysis"):
                with gr.Row():
                    with gr.Column(scale=1):
                        face_input = gr.Image(label="Image", type='filepath', elem_classes="example-image")
                        gr.Examples([os.path.join(root_path,'examples/att_1.jpg'),
                                    os.path.join(root_path,'examples/att_2.jpg'),
                                    os.path.join(root_path,'examples/att_3.jpg'),
                                    os.path.join(root_path,'examples/att_4.jpg'),
                                    os.path.join(root_path,'examples/att_5.jpg')],
                                    inputs=face_input)

                    with gr.Blocks():
                        with gr.Column(scale=1, elem_classes="block-background"):     
                            analyze_face_button = gr.Button("Analyze Face", variant="primary", size="lg")
                            with gr.Row(elem_classes="face-row"):
                                face_output = gr.Image(value=os.path.join(dir_path,'icons/face.jpg'), label="Face", scale=0, elem_classes="face-image")
                            
                            liveness_result = gr.Markdown("")
                            attribute_result = gr.Markdown("")
                        
                        analyze_face_button.click(analyze_face_clicked, inputs=face_input, outputs=[face_output, liveness_result, attribute_result])
        
    demo.launch(server_name="0.0.0.0", server_port=7860, show_api=False)

if __name__ == '__main__':
    g_activation_result = activate_sdk()
    launch_demo(g_activation_result)