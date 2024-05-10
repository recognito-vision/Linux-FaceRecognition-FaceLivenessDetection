<a href="https://recognito.vision" style="display: flex; align-items: center;">
    <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/b82f5c35-09d0-4064-a252-4bcd14e22407"/>
</a><br/>

# Face Liveness Detection SDK Demo for eKYC
<p align="center"><img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/468618e5-958e-4e00-b849-eac208c9f20b" alt="face liveness detection" width="80%"></p>

This demo showcases the capabilities of our Face Liveness Detection SDK, specifically tailored for Electronic Know Your Customer (eKYC) systems. With this SDK, you can perform **accurate** and **deepfake detectable** face liveness detection tasks on Linux platforms, enabling seamless integration into eKYC workflows.

Our [**Product List**](https://github.com/recognito-vision/Product-List/) for ID verification.

## <img src="https://github.com/recognito-vision/.github/assets/153883841/dc7c1c3f-8269-475c-a689-cb57be36a920" alt="home" width="25">   RECOGNITO Product Documentation
&emsp;&emsp;<a href="https://docs.recognito.vision" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/05/book.png" style="width: 64px; margin-right: 5px;"/></a>

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/4a0a6933-5236-4c72-ba24-306d299b2123" alt="system" width="25">  System Requirements

- **Operating System:** Ubuntu 20.04 or later
- **CPU:** 8 cores
- **RAM:** 8 GB
- **HDD:** 8 GB

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/2a625f6c-c8f1-49f6-87d3-f5f1477111cf" alt="docker" width="25">  Docker

  Pull the Docker image and run the container:
    
  ```
  sudo docker pull recognito/face-liveness:latest
  sudo docker run -it -e FL_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX" -p 8001:8000 -p 7861:7860 recognito/face-liveness:latest [OPTION --gradio(-g), --flask(-f)]
  ```

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/cd7a78b3-78da-4bd0-b12d-11771ab7345b" alt="install" width="25">  Installation

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection.git
    ```

2. Navigate to the directory of the SDK demo.
   ```
   cd Linux-FaceRecognition-FaceLivenessDetection/LivenessDetection-Demo
   ```

4. Run the `install.sh` script to install dependencies:

    ```
    ./install.sh
    ```

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/1c0d0786-c03f-42f2-9f9f-d9bf91778162" alt="install" width="25">  Setting Up SDK License Key  (Trial License Available)

- **Request to download `face-liveness_engine.zip` file from [here](https://drive.google.com/file/d/1pfhTxN3g_NCLWw_i6LLURLrx7zIFBCiy/view?usp=drive_link) and unzip in demo directory**
    ```
    unzip face-liveness_engine.zip 
    ```
- **Online Licensing:**
    Set the online license key as an environment variable:

    ```
    export FL_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX"
    ```

- **Offline Licensing:**
    Copy the `license.txt` license file to the demo directory. 
    For offline licensing, you must first provide us with the **Hardware ID** of your machine. 
    You can get your Hardware ID when running demos.
  
  <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/36a0b4ef-0ecc-49e6-af2c-29da86e41056" alt="HWID" width="80%"><br/>
  
  <div style="display: flex; align-items: center;">
        &nbsp;<a target="_blank" href="mailto:hassan@recognito.vision"><img src="https://img.shields.io/badge/email-hassan@recognito.vision-blue.svg?logo=gmail " alt="www.recognito.vision"></a>
        &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://wa.me/+14158003112"><img src="https://img.shields.io/badge/whatsapp-+14158003112-blue.svg?logo=whatsapp " alt="www.recognito.vision"></a>
        &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://t.me/recognito_vision"><img src="https://img.shields.io/badge/telegram-@recognito__vision-blue.svg?logo=telegram " alt="www.recognito.vision"></a>
        &nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://join.slack.com/t/recognito-workspace/shared_invite/zt-2d4kscqgn-"><img src="https://img.shields.io/badge/slack-recognito__workspace-blue.svg?logo=slack " alt="www.recognito.vision"></a>
   </div>

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/7ed1f28b-bb29-4c83-809c-015e2f8e38ad" alt="install" width="25">  Running Demo

- **Flask and Gradio Demo:**
    Run the demo script with the desired options:

    ```
    ./run_demo.sh [OPTION --gradio(-g), --flask(-f), --help(-h)]
    ```
    <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/51091e4c-79ea-4e5e-8b6b-1f6d8e34f665" alt="liveness-flask" width="80%">
    <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/af932c59-4f9d-471e-80af-d38cad483391" alt="liveness-gradio" width="80%">

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/c71602a2-cdca-4214-9bef-2997765b74a2" alt="chrome" width="25">  Testing

- **Flask:**
    To test the API, you can use [Postman](https://www.postman.com/downloads/). Here are the endpoints for testing:

    - `http://{xx.xx.xx.xx}:8000/api/check_liveness`
    - `http://{xx.xx.xx.xx}:8000/api/check_liveness_base64`
    
    If testing in **Docker** container, use the URL `http://{xx.xx.xx.xx}:8001/` instead of port 8000.

    <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/fb629a5f-83ec-42da-baf1-e6758554296b" alt="liveness-postman" width="90%">

- **Gradio:**
    Go to [http://127.0.0.1:7860/](http://127.0.0.1:7860/) on a web browser. If testing in **Docker** container, use the URL `http://{xx.xx.xx.xx}:7861/` instead of port 7860.

  <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/52238e52-73bf-4031-bfca-f71fb99c56a2" alt="faceliveness-gradio" width="90%">

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

