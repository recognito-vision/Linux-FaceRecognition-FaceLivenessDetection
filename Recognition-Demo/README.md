<a href="https://recognito.vision" style="display: flex; align-items: center;">
    <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/b82f5c35-09d0-4064-a252-4bcd14e22407"/>
</a><br/>

# Face Recognition SDK Demo for eKYC
<p align="center"><img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/37428b06-fe7c-4537-9875-d9701a5975e8" alt="face recognition" width="80%"></p>

This demo showcases the capabilities of our Face Recognition SDK with [**NIST FRVT Top 1 Face Recognition Algorithm**](https://pages.nist.gov/frvt/html/frvt11.html), specifically tailored for Electronic Know Your Customer (eKYC) systems. With this SDK, you can perform **accurate** face recognition tasks on Linux platforms, enabling seamless integration into eKYC workflows.

For more details and documentation, visit [https://docs.recognito.vision/](https://docs.recognito.vision/).

## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/4a0a6933-5236-4c72-ba24-306d299b2123" alt="system" width="25">  System Requirements

- **Operating System:** Ubuntu 20.04 or later
- **CPU:** 8 cores
- **RAM:** 8 GB
- **HDD:** 8 GB

## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/2a625f6c-c8f1-49f6-87d3-f5f1477111cf" alt="docker" width="25">  Docker

  Pull the Docker image and run the container:
    
  ```
  sudo docker pull recognito/face-recognition:latest
  sudo docker run -it -e FR_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX" -p 8001:8000 -p 7861:7860 recognito/face-recognition:latest [OPTION --gradio(-g), --flask(-f)]
  ```

## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/cd7a78b3-78da-4bd0-b12d-11771ab7345b" alt="install" width="25">  Installation

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection.git
    ```

2. Navigate to the directory of the SDK demo.
   ```
   cd Linux-FaceRecognition-FaceLivenessDetection/Recognition-Demo
   ```

4. Run the `install.sh` script to install dependencies:

    ```
    ./install.sh
    ```

## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/1c0d0786-c03f-42f2-9f9f-d9bf91778162" alt="install" width="25">  Setting Up SDK License Key  (Trial License Available)

- **Request to download `face-recognition_engine.zip` file from [here](https://drive.google.com/file/d/1Nwcfytl9ODIY78irjR-0Sdr5-whrkUPW/view?usp=drive_link) and unzip in demo directory**
    ```
    unzip face-recognition_engine.zip 
    ```
- **Online Licensing:**
    Set the online license key as an environment variable:

    ```
    export FR_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX"
    ```

- **Offline Licensing:**
    Copy the `license.txt` license file to the demo directory. 
    For offline licensing, you must first provide us with the **Hardware ID** of your machine. 
    You can get your Hardware ID when running demos.
  
  <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/82b976d3-ee16-4266-aeb0-c1e80898cfed" alt="HWID" width="80%"><br/>
  <div style="display: flex; align-items: center;">
    <a target="_blank" href="mailto:hassan@recognito.vision"><img src="https://img.shields.io/badge/email-hassan@recognito.vision-blue.svg?logo=gmail " alt="www.recognito.vision"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://wa.me/+14158003112"><img src="https://img.shields.io/badge/whatsapp-+14158003112-blue.svg?logo=whatsapp " alt="www.recognito.vision"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://t.me/recognito_vision"><img src="https://img.shields.io/badge/telegram-@recognito__vision-blue.svg?logo=telegram " alt="www.recognito.vision"></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://join.slack.com/t/recognito-workspace/shared_invite/zt-2d4kscqgn-"><img src="https://img.shields.io/badge/slack-recognito__workspace-blue.svg?logo=slack " alt="www.recognito.vision"></a>
  </div>
## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/7ed1f28b-bb29-4c83-809c-015e2f8e38ad" alt="install" width="25">  Running Demo

- **Flask and Gradio Demo:**
    Run the demo script with the desired options:

    ```
    ./run_demo.sh [OPTION --gradio(-g), --flask(-f), --help(-h)]
    ```
    <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/cf9893c7-751a-42d8-a098-21ba3f3f6e8f" alt="recognition-flask" width="80%">
    <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/6adf1ed2-a701-47c2-9a3c-2f6f82487aad" alt="recognition-gradio" width="80%">

## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/c71602a2-cdca-4214-9bef-2997765b74a2" alt="chrome" width="25">  Testing

- **Flask:**
    To test the API, you can use [Postman](https://www.postman.com/downloads/). Here are the endpoints for testing:
  
    - `http://{xx.xx.xx.xx}:8000/api/compare_face`
    - `http://{xx.xx.xx.xx}:8000/api/compare_face_base64`
    
    If testing in **Docker** container, use the URL `http://{xx.xx.xx.xx}:8001/` instead of port 8000.

    <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/e2e1d94e-e8c9-4839-9fa7-2f3365aafc75" alt="postman" width="90%">

- **Gradio:**
    Go to [http://127.0.0.1:7860/](http://127.0.0.1:7860/) on a web browser. If testing in **Docker** container, use the URL `http://{xx.xx.xx.xx}:7861/` instead of port 7860.

    <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/1c625cdc-8074-4f49-8daa-3cdb9e667e30" alt="facerecognition-gradio" width="90%">

## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/78c5efee-15f3-4406-ab4d-13fd1182d20c" alt="contact" width="25">  Contact Us

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
    &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://huggingface.co/Recognito" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/hf_64_cl.png" style="width: 32px; margin-right: 5px;"/></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/Recognito-Vision" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/github_64_cl.png" style="width: 32px; margin-right: 5px;"/></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://hub.docker.com/u/recognito" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/03/docker_64_cl.png" style="width: 32px; margin-right: 5px;"/></a>
    &nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.youtube.com/@Recognito-Ltd" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/04/youtube_64_cl.png" style="width: 32px; margin-right: 5px;"/></a>
</p>
