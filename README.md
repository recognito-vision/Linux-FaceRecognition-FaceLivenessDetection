<div>
    <a href="https://recognito.vision">
        <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/b82f5c35-09d0-4064-a252-4bcd14e22407"/>
    </a>
    <a href="https://trendshift.io/repositories/9612" target="_blank">
        <img src="https://trendshift.io/api/badge/repositories/9612" alt="Recognito-Vision%2FLinux-FaceRecognition-FaceLivenessDetection" style="float: right; width: 250px; height: 55px;" width="250" height="55" align="right"/>
    </a>
</div>
<br/>

<p align="center">
    <img alt="" src="https://recognito.vision/wp-content/uploads/2024/03/NIST.png" width=90%/>
</p>
<p align="center" style="font-size: 24px; font-weight: bold;">
    <a href="https://pages.nist.gov/frvt/html/frvt11.html" target="_blank">
        Latest NIST FRVT Report
    </a>  
</p>

### 📰 _Recognito Developer News_
- <img src="https://github.com/user-attachments/assets/59da5e7c-9a2e-40c4-821b-5b1e05fb905b" alt="home" width="30"> 1:1 & 1:N [**Windows .NET Demo for Face Recognition, Liveness Detection**](https://github.com/recognito-vision/FaceRecognition-LivenessDetection-CSharp-.Net).
- Global Coverage [**ID Card/Passport OCR Mobile Demo**](https://github.com/recognito-vision/Android-ID-Document-Recognition/tree/main) and [**ID Document Recognition Server Demo**](https://github.com/recognito-vision/Linux-ID-Document-Recognition).
- Try **1:N Face Search** through our [**Face Identification Web Demo**](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/Identification(1%3AN)-Demo).
- Subscribe our **Free APIs** for your app or website from our [**API Hub**](https://rapidapi.com/organization/recognito).
<!--- Clone our [**Hugging Face space**](https://huggingface.co/recognito) for your IDV project setup.-->
<br/>

# On-Premise Face Recognition, Liveness Detection, Face Attribute Analysis SDK Demo (Linux Server)

Welcome to our Face SDK Demos repository! Here you will find demos showcasing the capabilities of our on-premise Face SDKs, including face recognition, liveness detection, and face attribute analysis. Our SDK is designed to work seamlessly on **Linux** Server platforms and can be integrated into various systems such as **eKYC** solutions and **CCTV** systems.

Our [**Product List**](https://github.com/recognito-vision/Product-List/) for ID verification.

## <img src="https://github.com/recognito-vision/.github/assets/153883841/dc7c1c3f-8269-475c-a689-cb57be36a920" alt="home" width="25">   RECOGNITO Product Documentation
&emsp;&emsp;<a href="https://docs.recognito.vision" style="display: flex; align-items: center;"><img src="https://recognito.vision/wp-content/uploads/2024/05/book.png" style="width: 64px; margin-right: 5px;"/></a>

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/d0991c83-44f0-4d38-bcc8-74376ce93ded" alt="feature" width="25">  Features
- **Face Recognition:** Identify and verify individuals by comparing their facial features.
- **Liveness Detection:** Determine whether a face is live or spoofed to prevent fraud in authentication processes.
- **Face Attribute Analysis:** Extract facial attributes such as age, gender, emotion, and ethnicity from facial images for demographic analysis.

<p align="center"><img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/37428b06-fe7c-4537-9875-d9701a5975e8" alt="face recognition" width="80%"></p>

<p align="center"><img src="https://github.com/user-attachments/assets/74c6d41a-4ccb-4d36-b506-5c5eb1c4ae2d" alt="face liveness detection" width="80%"></p>

<p align="center"><img src="https://github.com/user-attachments/assets/620c3dda-bc89-4f34-a391-eccd8826e093" alt="face identification" width="80%"></p>

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/2a625f6c-c8f1-49f6-87d3-f5f1477111cf" alt="docker" width="25">  Docker

  Pull the Docker image from [hub.docker.com/recognito](https://hub.docker.com/u/recognito) and run the container:

  | No.      | Demo | Docker Image | Commands | Request License |
  |:------------------:|------------------|------------------|------------------|:------------------:|
  |1         | [Face Recognition for eKYC](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/Recognition-Demo) | recognito/face-recognition:latest |`sudo docker pull recognito/face-recognition:latest`<br> `sudo docker run -it -e FR_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX" -p 8001:8000 -p 7861:7860 recognito/face-recognition:latest [OPTION --gradio(-g), --flask(-f)]`| [Send](mailto:hassan@recognito.vision)|
  |2         | [Face Liveness Detection for eKYC](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/LivenessDetection-Demo) | recognito/face-liveness:latest |`sudo docker pull recognito/face-liveness_v7:latest` <br> `sudo docker run -it -e FL_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX" -p 8001:8000 -p 7861:7860 recognito/face-liveness_v7:latest [OPTION --gradio(-g), --flask(-f)]`|[Send](mailto:hassan@recognito.vision)|
  |3         | [Face SDK Lite for CCTV](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/FaceSDK-Lite-Demo) | recognito/facesdk-lite:latest | `sudo docker pull recognito/facesdk-lite:latest` <br> `sudo docker run -it -v ./license.txt:/home/recognito_lite/license.txt -p 8001:8000 -p 7861:7860 recognito/facesdk-lite:latest [OPTION --gradio(-g), --flask(-f)]`|[Send](mailto:hassan@recognito.vision)|

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/c15b7c1d-346f-4b0b-ad1e-c65882b14d27" alt="list" width="25">  Face SDK Demo List
  | No.      | Demo | SDK Details | Download Demo (zip) and Trial license | Installation Guide | 
  |:------------------:|------------------|------------------|:------------------:|:------------------:|
  | 1        | [Face Recognition](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/Recognition-Demo)    | Face Recognition for eKYC | [Download](https://drive.google.com/file/d/1vZu085YimHuqvGA0dIXbyIZTjYndGfeT/view?usp=drive_link) | [Installation](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/Recognition-Demo)    |
  | 2        | [Face Identification](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/Identification(1%3AN)-Demo)    | Face Identification for 1:N Search | [Download](https://drive.google.com/file/d/1-Fr79Mj6glGtcqVEXXLGwwEWG8DCffsF/view?usp=drive_link) | [Installation](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/Identification(1%3AN)-Demo)    |
  | 3        | [Face Liveness Detection](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/LivenessDetection-Demo)    | Face Liveness Detection for eKYC | [Download](https://drive.google.com/file/d/1IM8NcJwYyBOQIqKcNVqWtpSca0hpsbpa/view?usp=drive_link) | [Installation](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/LivenessDetection-Demo) |
  | 4        | [Face SDK Lite](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/FaceSDK-Lite-Demo)    | Face Recognition, Liveness Detection for CCTV system | [Download](https://drive.google.com/file/d/1pRSvJM2wVyH2rrvBq_276y4QgaIFAWir/view?usp=drive_link) | [Installation](https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/tree/main/FaceSDK-Lite-Demo)   |

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/4a0a6933-5236-4c72-ba24-306d299b2123" alt="system" width="25">  System Requirements
 - **Linux OS:** Ubuntu 20.04 or 22.04
 - **CPU:** 8 cores
 - **RAM:** 8 GB
 - **HDD:** 8 GB

## <img src="https://github.com/recognito-vision/Linux-FaceRecognition-FaceLivenessDetection/assets/153883841/78c5efee-15f3-4406-ab4d-13fd1182d20c" alt="contact" width="25">  Support
For any questions, issues, or feature requests, please contact our support team.

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
