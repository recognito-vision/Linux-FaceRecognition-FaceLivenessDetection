<a href="https://recognito.vision" style="display: flex; align-items: center;">
    <img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/b82f5c35-09d0-4064-a252-4bcd14e22407"/>
</a><br/>

# Face Recognition SDK Demo for eKYC
<p align="center"><img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/37428b06-fe7c-4537-9875-d9701a5975e8" alt="face recognition" width="80%"></p>

This demo showcases the capabilities of our Face Recognition SDK, specifically tailored for Electronic Know Your Customer (eKYC) systems. With this SDK, you can perform accurate face recognition tasks on Linux platforms, enabling seamless integration into eKYC workflows.

For more details and documentation, visit [https://docs.recognito.vision/](https://docs.recognito.vision/).

## <img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/4a0a6933-5236-4c72-ba24-306d299b2123" alt="system" width="25">  System Requirements

- **Operating System:** Ubuntu 20.04 or later
- **CPU:** 8 cores
- **RAM:** 8 GB
- **HDD:** 8 GB

## <img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/2a625f6c-c8f1-49f6-87d3-f5f1477111cf" alt="docker" width="25">  Docker


  Pull the Docker image and run the container:
    
  ```
  sudo docker pull recognito/face-recognition:latest
  sudo docker run -it -e FR_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX" -p 8001:8000 -p 7861:7860 recognito/face-recognition:latest [OPTION --gradio(-g), --flask(-f)]
  ```
## <img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/cd7a78b3-78da-4bd0-b12d-11771ab7345b" alt="install" width="25">  Installation

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/Recognito-Vision/Face-SDK-Linux-Demos.git
    ```

2. Navigate to the directory of the SDK demo.
   ```
   cd Face-SDK-Linux-Demos/Recognition-Demo
   ```

4. Run the install.sh script to install dependencies:

    ```
    ./install.sh
    ```

## <img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/1c0d0786-c03f-42f2-9f9f-d9bf91778162" alt="install" width="25">  Setting Up SDK License Key
- **Request to download face-recognition_engine.zip file from [here](https://drive.google.com/file/d/1Y3TCnDnrG0kvqrTECff3fhN8-WxdcaO_/view?usp=drive_link) and unzip in demo directory**
    ```
    unzip face-recognition_engine.zip 
    ```
- **Online Licensing:**
    Set the online license key as an environment variable:

    ```
    export FR_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX"
    ```

- **Offline Licensing:**
    Copy the 'license.txt' license file to the demo directory. 
    For offline licensing, you must first provide us with the hardware ID of your machine. 
    You can get your Hardware ID when running demos.
      <img src="https://github.com/Recognito-Vision/Face-SDK-Linux-Demos/assets/153883841/82b976d3-ee16-4266-aeb0-c1e80898cfed" alt="HWID" width="80%">

## Running Demo

- **Flask and Gradio Demo:**
    Run the demo script with the desired options:

    ```
    ./run_demo.sh [OPTION --gradio(-g), --flask(-f), --help(-h)]
    ```
## Testing

- **Flask:**
    To test the API, you can use Postman. Here are the endpoints for testing:

    - Test with image files: Send a POST request with [image1], [image2] in form-data format to `http://{xx.xx.xx.xx}:8000/api/compare_face`.
    - Test with base64-encoded images: Send a POST request with [image1], [image2] in raw format to `http://{xx.xx.xx.xx}:8000/api/compare_face_base64`.
    
    If testing in Docker container, use the URL `http://{xx.xx.xx.xx}:8001/` instead of port 8000.

- **Gradio:**
    Run `http://{xx.xx.xx.xx}:7860/` on a web browser. If testing in Docker container, use the URL `http://{xx.xx.xx.xx}:7861/` instead of port 7860.

## Contact Information

If you encounter any issues or have any questions, please feel free to contact us:

- **Email:** hassan@recognito.vision
- **WhatsApp:** +14158003112
- **Telegram:** @recognito_vision

