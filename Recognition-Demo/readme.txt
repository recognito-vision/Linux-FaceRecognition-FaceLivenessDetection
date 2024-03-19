Guide - Face Recognition Linux for eKYC

Read more details on https://docs.recognito.vision/

1. System OS, Requirements 
  - OS: Ubuntu 20.04 or later
  - Requirements
    CPU: 4 cores or more (Recommended: 8 cores)
    RAM: 4 GB or more (Recommended: 8 GB)
    HDD: 4 GB or more (Recommended: 8 GB)
2. Installation of dependency
  - Run the install.sh script.
    ./install.sh
3. Set SDK license key (online or offline mode)
  - Online: Set online license key as an environment variable.
    export FR_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX"
  - Offline: Copy 'license.txt' license file to the work directory
    For offline licensing, you must first provide us with the hardware ID of your machine.
    You can get your Hardware ID when running demos.

4. Run demo
  - Run flask, gradio demo script
    ./run_demo.sh [OPTION --gradio(-g), --flask(-f), --help(-h)]
  - Docker
    sudo docker pull recognito/face-recognition:latest
    sudo docker run -it -e FR_LICENSE_KEY="XXXXX-XXXXX-XXXXX-XXXXX" -p 8001:8000 -p 7861:7860 recognito/face-recognition:latest [OPTION --gradio(-g), --flask(-f)]

5. Test 
  - Flask
    To test the API, you can use Postman. Here are the endpoints for testing:
    Test with image files: Send a POST request with [image1], [image2] in form-data format to http://{xx.xx.xx.xx}:8000/api/compare_face.
        e.g. http://127.0.0.1:8000/api/compare_face
    Test with base64-encoded images: Send a POST request with [image1], [image2] in raw format to http://{xx.xx.xx.xx}:8000/api/compare_face_base64.
    If testing in Docker container, use the URL http://{xx.xx.xx.xx}:8001/ instead of 8000 PORT.
  - Gradio
    Run http://{xx.xx.xx.xx}:7860/ on web browser.
        e.g. http://127.0.0.1:7860/
    If testing in Docker container, use the URL http://{xx.xx.xx.xx}:7861/ instead of 7860 PORT.

6. Contact us if any issue
    email:      hassan@recognito.vision
    whatsapp:   +14158003112
    telegram:   @recognito_vision
