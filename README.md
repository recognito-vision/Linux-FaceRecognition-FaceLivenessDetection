<a href="https://recognito.vision" style="display: flex; align-items: center;">
    <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/b82f5c35-09d0-4064-a252-4bcd14e22407"/>
</a><br/><br/>
<p align="center">
    <img alt="" src="https://recognito.vision/wp-content/uploads/2024/03/NIST.png" width=90%/>
</p>
<p align="center" style="font-size: 24px; font-weight: bold;">
    <a href="https://pages.nist.gov/frvt/html/frvt11.html" target="_blank">
        Latest NIST FRVT Report
    </a>  
</p>

# On-Premise Face Recognition, Liveness Detection, Face Attribute Analysis SDK Demo (Linux Server)
Welcome to our Face SDK Demos repository! Here you will find demos showcasing the capabilities of our on-premise Face SDKs, including face recognition, liveness detection, and face attribute analysis. Our SDK is designed to work seamlessly on Linux Server platforms and can be integrated into various systems such as eKYC solutions and CCTV systems.

## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/d0991c83-44f0-4d38-bcc8-74376ce93ded" alt="feature" width="25">  Features
- **Face Recognition:** Identify and verify individuals by comparing their facial features.
- **Liveness Detection:** Determine whether a face is live or spoofed to prevent fraud in authentication processes.
- **Face Attribute Analysis:** Extract facial attributes such as age, gender, emotion, and ethnicity from facial images for demographic analysis.

## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/2a625f6c-c8f1-49f6-87d3-f5f1477111cf" alt="docker" width="25">  Docker

  Pull the Docker image from [hub.docker.com/recognito](https://hub.docker.com/u/recognito) and run the container:

  | No.      | Demo | Docker Image | Commands | Request License |
  |:------------------:|------------------|------------------|------------------|:------------------:|
  |1         | [Face Recognition for eKYC](https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/Recognition-Demo) | recognito/face-recognition:latest |`sudo docker pull recognito/face-recognition:latest`<br> `sudo docker run -it -e FR_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX" -p 8001:8000 -p 7861:7860 recognito/face-recognition:latest [OPTION --gradio(-g), --flask(-f)]`| [Send](mailto:hello@recognito.vision)|
  |2         | [Face Liveness Detection for eKYC](https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/LivenessDetection-Demo) | recognito/face-liveness:latest |`sudo docker pull recognito/face-liveness:latest` <br> `sudo docker run -it -e FL_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX" -p 8001:8000 -p 7861:7860 recognito/face-liveness:latest [OPTION --gradio(-g), --flask(-f)]`|[Send](mailto:hello@recognito.vision)|
  |3         | [Face SDK Lite for CCTV](https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/FaceSDK-Lite-Demo) | recognito/facesdk-lite:latest | `sudo docker pull recognito/facesdk-lite:latest` <br> `sudo docker run -it -v ./license.txt:/home/recognito_lite/license.txt -p 8001:8000 -p 7861:7860 recognito/facesdk-lite:latest [OPTION --gradio(-g), --flask(-f)]`|[Send](mailto:hello@recognito.vision)|

## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/c15b7c1d-346f-4b0b-ad1e-c65882b14d27" alt="list" width="25">  Face SDK Demo List
  | No.      | Demo | SDK Details | Download Demo (zip) and Trial license |
  |:------------------:|------------------|------------------|:------------------:|
  | 1        | [Face Recognition](https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/Recognition-Demo)    | Face Recognition for eKYC | [Download](https://drive.google.com/file/d/1vZu085YimHuqvGA0dIXbyIZTjYndGfeT/view?usp=drive_link) |
  | 2        | [Face Liveness Detection](https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/LivenessDetection-Demo)    | Face Liveness Detection for eKYC | [Download](https://drive.google.com/file/d/1R0Bus5XthpV5Qodq5Yp22n6Uyad9M-Jt/view?usp=drive_link) |
  | 3        | [Face SDK Lite](https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/FaceSDK-Lite-Demo)    | Face Recognition, Liveness Detection for CCTV system | [Download](https://drive.google.com/file/d/1pRSvJM2wVyH2rrvBq_276y4QgaIFAWir/view?usp=drive_link) |

## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/4a0a6933-5236-4c72-ba24-306d299b2123" alt="system" width="25">  System Requirements
 - **Linux OS:** Ubuntu 20.04 or later
 - **CPU:** 8 cores
 - **RAM:** 8 GB
 - **HDD:** 8 GB

## <img src="https://github.com/Recognito-Vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/78c5efee-15f3-4406-ab4d-13fd1182d20c" alt="contact" width="25">  Support
For any questions, issues, or feature requests, please contact our support team.

<div style="display: flex; align-items: center;">
    <a target="_blank" href="mailto:hello@recognito.vision"><img src="https://img.shields.io/badge/email-hassan@recognito.vision-blue.svg?logo=gmail " alt="www.recognito.vision"></a>
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
