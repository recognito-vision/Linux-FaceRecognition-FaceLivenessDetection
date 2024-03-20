# Face SDK Lite Linux for CCTV System

Welcome to the Face SDK Lite for Linux designed for CCTV systems. This guide will help you set up and run the Face SDK Lite on your Ubuntu 20.04 or later system. For more detailed information, please refer to our [documentation](https://docs.recognito.vision/).

## System Requirements

- **Operating System:** Ubuntu 20.04 or later
- **CPU:** 4 cores or more (Recommended: 8 cores)
- **RAM:** 4 GB or more (Recommended: 8 GB)
- **HDD:** 4 GB or more (Recommended: 8 GB)

## Installation of Dependencies

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

## Setting Up SDK License Key

1. Copy the 'license.txt' license file to the work directory.

   For licensing, you must first provide us with the hardware ID of your machine. You can get your Hardware ID when running demos.

## Running Demo

- **Flask and Gradio Demo:**
    Run the demo script with the desired options:

    ```
    ./run_demo.sh [OPTION --gradio(-g), --flask(-f), --help(-h)]
    ```

- **Using Docker:**
    Pull the Docker image and run the container:

    ```
    sudo docker pull recognito/facesdk-lite:latest
    sudo docker run -it -v ./license.txt:/home/recognito_lite/license.txt -p 8001:8000 -p 7861:7860 recognito/facesdk-lite:latest [OPTION --gradio(-g), --flask(-f)]
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
