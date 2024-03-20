<a href="https://recognito.vision" style="display: flex; align-items: center;">
    <img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/b82f5c35-09d0-4064-a252-4bcd14e22407"/>
</a><br/>

# Face SDK Lite Linux for CCTV System
<p align="center"><img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/b120e4f1-b53b-4b7d-ad38-cd3436b8f75a" alt="face recognition" width="80%"></p>
<p align="center"><img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/07f876cd-8f13-4101-9cf1-414683eb985a" alt="face liveness" width="80%"></p>

This demo showcases the capabilities of our Face Recognition, Liveness Detection, Face Attribute Analysis Lite SDK for Linux designed for CCTV systems. For more detailed information, please refer to our [documentation](https://docs.recognito.vision/).

## <img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/4a0a6933-5236-4c72-ba24-306d299b2123" alt="system" width="25">  System Requirements

- **Operating System:** Ubuntu 20.04 or later
- **CPU:** 8 cores
- **RAM:** 8 GB
- **HDD:** 8 GB

## <img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/2a625f6c-c8f1-49f6-87d3-f5f1477111cf" alt="docker" width="25">  Docker

    Pull the Docker image and run the container:
    
    ```
    sudo docker pull recognito/facesdk-lite:latest
    sudo docker run -it -v ./license.txt:/home/recognito_lite/license.txt -p 8001:8000 -p 7861:7860 recognito/facesdk-lite:latest [OPTION --gradio(-g), --flask(-f)]
    ```

## <img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/cd7a78b3-78da-4bd0-b12d-11771ab7345b" alt="install" width="25">  Installation

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/Recognito-Vision/Face-SDK-Linux-Demos.git
    ```

2. Navigate to the directory of the SDK.
   ```
   cd Face-SDK-Linux-Demos/FaceSDK-Lite-Demo
   ```

4. Run the install.sh script to install dependencies:

    ```
    ./install.sh
    ```

## <img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/1c0d0786-c03f-42f2-9f9f-d9bf91778162" alt="install" width="25">  Setting Up SDK License Key
- **Request to download facesdk-lite_engine.zip file from [here](https://drive.google.com/file/d/1oyPOvETwQYXajuTKHkZMAFfO-nR712lU/view?usp=drive_link) and unzip in demo directory**
    ```
    unzip facesdk-lite_engine.zip
    ```

- **Licensing:**
    Copy the 'license.txt' license file to the work directory.
    For licensing, you must first provide us with the hardware ID of your machine. You can get your Hardware ID when running demos.

## Running Demo

- **Flask and Gradio Demo:**
    Run the demo script with the desired options:

    ```
    ./run_demo.sh [OPTION --gradio(-g), --flask(-f), --help(-h)]
    ```

## Testing

- **Flask:**
    To test the API, you can use Postman. Here are the endpoints for testing:

    - Test face recognition with image files: Send a POST request with [image1], [image2] in form-data format to `http://{xx.xx.xx.xx}:8000/api/compare_face`.
    - Test face analysis with image file: Send a POST request with [image] in form-data format to `http://{xx.xx.xx.xx}:8000/api/analyze_face`.
    
    If testing in Docker container, use the URL `http://{xx.xx.xx.xx}:8001/` instead of port 8000.

- **Gradio:**
    Run `http://{xx.xx.xx.xx}:7860/` on a web browser. If testing in Docker container, use the URL `http://{xx.xx.xx.xx}:7861/` instead of port 7860.

## Contact Information

If you encounter any issues or have any questions, please feel free to contact us:

- **Email:** hassan@recognito.vision
- **WhatsApp:** +14158003112
- **Telegram:** @recognito_vision
