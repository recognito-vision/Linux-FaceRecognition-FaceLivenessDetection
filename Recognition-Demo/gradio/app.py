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
gradio_path = os.path.dirname(file_path)
root_path = os.path.dirname(gradio_path)

version = get_version().decode('utf-8')
print_info('\t <Recognito Face Recognition> \t version {}'.format(version))

device_id = get_deviceid().decode('utf-8')
print_info('\t <Hardware ID> \t\t {}'.format(device_id))

g_activation_result = -1
MATCH_THRESHOLD = 0.67

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

.block-background {
    # background-color: #202020; /* Set your desired background color */
    border-radius: 5px;
}

"""

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
    result, score, face_bboxes, face_features = compare_face(image_mat1, image_mat2, float(threshold))
    end_time = time.time()
    process_time = (end_time - start_time) * 1000

    try:
        image1 = Image.open(frame1)
        image2 = Image.open(frame2)
        images = [image1, image2]

        face1 = Image.new('RGBA',(150, 150), (80,80,80,0))
        face2 = Image.new('RGBA',(150, 150), (80,80,80,0))
        faces = [face1, face2]

        face_bboxes_result = []

        if face_bboxes is None:
            gr.Warning(result)
            return None, None, None, None, None, None, None, None, None
        else:
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
        
    matching_result = Image.open(os.path.join(gradio_path, "icons/blank.png"))
    similarity_score = ""

    if score is not None:
        str_score = str("{:.4f}".format(score))
        if result == "SAME PERSON":
            matching_result = Image.open(os.path.join(gradio_path, "icons/same.png"))
            similarity_score = f"""<br/><div class="markdown-success-container"><p style="text-align: center; font-size: 20px; color: green;">Similarity score: {str_score}</p></div>"""
        else:
            matching_result = Image.open(os.path.join(gradio_path, "icons/different.png"))
            similarity_score = f"""<br/><div class="markdown-fail-container"><p style="text-align: center; font-size: 20px; color: red;">Similarity score: {str_score}</p></div>"""

    return faces[0], faces[1], matching_result, similarity_score, face_bboxes_result[0], face_bboxes_result[1], face_features[0], face_features[1], str(process_time)

def launch_demo(activate_result):
    with gr.Blocks(css=css) as demo:
        gr.Markdown(
            f"""
            <a href="https://recognito.vision" style="display: flex; align-items: center;">
                <img src="https://recognito.vision/wp-content/uploads/2024/03/Recognito-modified.png" style="width: 3%; margin-right: 15px;"/>
            </a>
            <div style="display: flex; align-items: center;justify-content: center;">
                <p style="font-size: 36px; font-weight: bold;">Face Recognition {version}</p>
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
                        face_output1 = gr.Image(value=os.path.join(gradio_path,'icons/face.jpg'), label="Face 1", scale=0, elem_classes="face-image")
                        compare_result = gr.Image(value=os.path.join(gradio_path,'icons/blank.png'), min_width=30, scale=0, show_download_button=False, show_label=False)
                        face_output2 = gr.Image(value=os.path.join(gradio_path,'icons/face.jpg'), label="Face 2", scale=0, elem_classes="face-image")
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
            
    demo.launch(server_name="0.0.0.0", server_port=7860, show_api=False)

if __name__ == '__main__':
    g_activation_result = activate_sdk()
    launch_demo(g_activation_result)
