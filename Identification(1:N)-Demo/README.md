<a href="https://recognito.vision" style="display: flex; align-items: center;">
    <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/b82f5c35-09d0-4064-a252-4bcd14e22407"/>
</a><br/>

# Face Identification Flask Demo for 1:N search

<p align="center"><img src="https://github.com/user-attachments/assets/0f5d9d9d-60ab-4597-9f1a-344c20cb95fb" alt="face identification" width="80%"></p>

This demo showcases the capabilities of our Face Recognition SDK with [**NIST FRVT Top 1 Face Recognition Algorithm**](https://pages.nist.gov/frvt/html/frvt11.html). With our SDK, you can perform highly accurate **Face Search and Identification** tasks on Linux platforms, enabling seamless integration into diverse identity verification workflows.

Our [**Product List**](https://github.com/recognito-vision/Product-List/) for ID verification.

## <img src="https://github.com/recognito-vision/.github/assets/153883841/dc7c1c3f-8269-475c-a689-cb57be36a920" alt="home" width="25">   RECOGNITO Product Documentation
&emsp;&emsp;<a href="https://docs.recognito.vision" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/05/book.png" style="width: 64px; margin-right: 5px;"/></a>

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/4a0a6933-5236-4c72-ba24-306d299b2123" alt="system" width="25">  System Requirements

- **Operating System:** Ubuntu 20.04 or 22.04
- **CPU:** 8 cores
- **RAM:** 8 GB
- **HDD:** 8 GB

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/cd7a78b3-78da-4bd0-b12d-11771ab7345b" alt="install" width="25">  How run demo?

1. Download the Folder from google drive to your machine.

    https://drive.google.com/file/d/1-Fr79Mj6glGtcqVEXXLGwwEWG8DCffsF/view?usp=drive_link

2. Install packages
   ```
 	sudo apt-get update -y && sudo apt-get install -y python3 python3-pip python3-opencv libcurl4-openssl-dev libssl-dev libtbb-dev
	python3 -m pip install --upgrade pip && python3 -m pip install opencv-python 
   ```

4. Copy dependency libraries to /usr/lib.
    ```
    sudo cp -f dependency/libimutils.so /usr/lib/libimutils.so
	sudo cp -rf dependency/openvino /usr/lib
	export LD_LIBRARY_PATH="/usr/lib/openvino:$LD_LIBRARY_PATH"
    ```
    
6. Install requirements
    ```
	pip install -r requirements.txt
    ```
	
7. Run Qdrant server.
    ```
	sudo docker run --network="host" -v ./database:/qdrant/storage qdrant/qdrant:latest
    ```
	
8. Activate SDK with license
    ```
	export FR_LICENSE_KEY="xxxxx-xxxxx-xxxxx-xxxxx"
    ```
	
9. Run the web app.
    ```
	python3 app.py
    ```

10. Visit the http://127.0.0.1:9000 to view the web app
11. Qdrant Web UI http://127.0.0.1:6333/dashboard


## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/7ed1f28b-bb29-4c83-809c-015e2f8e38ad" alt="install" width="25">  How demo works?
![screen01](https://github.com/user-attachments/assets/535d6a37-06f4-4dc7-9e0b-8fea3fbf06ed)
![screen02](https://github.com/user-attachments/assets/7a72f08b-48b4-4307-8d8a-f54edeb8c986)
![screen05](https://github.com/user-attachments/assets/49a5169b-2889-48d1-b4b2-da75d24ef985)
![screen03](https://github.com/user-attachments/assets/3754aac0-2129-4d2a-b8e9-36b04385177a)
![screen04](https://github.com/user-attachments/assets/5716a180-e09e-4800-b92b-e45ff953e60f)


## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/78c5efee-15f3-4406-ab4d-13fd1182d20c" alt="contact" width="25">  Contact Us

For trial license or if you encounter any issues or have any questions, please feel free to contact us:

<div style="display: flex; align-items: center;">
    <a target="_blank" href="mailto:hassan@recognito.vision"><img src="https://img.shields.io/badge/email-hassan@recognito.vision-blue.svg?logo=gmail " alt="www.recognito.vision"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://wa.me/+14158003112"><img src="https://img.shields.io/badge/whatsapp-+14158003112-blue.svg?logo=whatsapp " alt="www.recognito.vision"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://t.me/recognito_vision"><img src="https://img.shields.io/badge/telegram-@recognito__vision-blue.svg?logo=telegram " alt="www.recognito.vision"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://join.slack.com/t/recognito-workspace/shared_invite/zt-2d4kscqgn-"><img src="https://img.shields.io/badge/slack-recognito__workspace-blue.svg?logo=slack " alt="www.recognito.vision"></a>
</div>
<br/>
<p align="center">
    &emsp;&emsp;<a href="https://recognito.vision" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/recognito_64_cl.png" style="width: 32px; margin-right: 5px;"/></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.linkedin.com/company/recognito-vision" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/linkedin_64_cl.png" style="width: 32px; margin-right: 5px;"/></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://huggingface.co/recognito" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/hf_64_cl.png" style="width: 32px; margin-right: 5px;"/></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/recognito-vision" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/github_64_cl.png" style="width: 32px; margin-right: 5px;"/></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://hub.docker.com/u/recognito" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/docker_64_cl.png" style="width: 32px; margin-right: 5px;"/></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.youtube.com/@recognito-vision" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/04/youtube_64_cl.png" style="width: 32px; margin-right: 5px;"/></a>
</p>
