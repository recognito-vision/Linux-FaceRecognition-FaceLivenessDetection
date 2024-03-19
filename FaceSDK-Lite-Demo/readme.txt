Guide - Face SDK Lite Linux for CCTV system

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
3. Set SDK license key
  - Copy 'license.txt' license file to the work directory
    For licensing, you must first provide us with the hardware ID of your machine.
    You can get your Hardware ID when running demos.

4. Run demo
  - Run flask, gradio demo script
    ./run_demo.sh [OPTION --gradio(-g), --flask(-f), --help(-h)]
  - Docker
    sudo docker pull recognito/facesdk-lite:latest
    sudo docker run -it -v ./license.txt:/home/recognito_lite/license.txt -p 8001:8000 -p 7861:7860 recognito/facesdk-lite:latest [OPTION --gradio(-g), --flask(-f)]

5. Test 
  - Flask
    To test the API, you can use Postman. Here are the endpoints for testing:
    Test face recognition with image files: Send a POST request with [image1], [image2] in form-data format to http://{xx.xx.xx.xx}:8000/api/compare_face.
        e.g. http://127.0.0.1:8000/api/compare_face
    Test face analysis with image file: Send a POST request with [image] in form-data format to http://{xx.xx.xx.xx}:8000/api/analyze_face.
    If testing in Docker container, use the URL http://{xx.xx.xx.xx}:8001/ instead of 8000 PORT.
  - Gradio
    Run http://{xx.xx.xx.xx}:7860/ on web browser.
        e.g. http://127.0.0.1:7860/
    If testing in Docker container, use the URL http://{xx.xx.xx.xx}:7861/ instead of 7860 PORT.

6. Contact us if any issue
    email:      hassan@recognito.vision
    whatsapp:   +14158003112
    telegram:   @recognito_vision
