#!/bin/sh

echo "Install environment..."

. /etc/os-release
ubuntu_version="$VERSION_ID"
echo "Ubuntu version: $ubuntu_version"

# Check if the version is 20.04 or later
if [ "$ubuntu_version" \< "20.04" ]; then
    # Print an error message and exit
    echo "Error: Ubuntu version must be 20.04 or later"
    exit 1
fi

# Install packages:
sudo apt-get update -y && sudo apt-get install -y python3 python3-pip python3-opencv libcurl4-openssl-dev libssl-dev libtbb-dev

# Install requirements:
python3 -m pip install --upgrade pip && python3 -m pip install opencv-python flask flask-cors gradio

# Copy libraries to /usr/lib based on Ubuntu version
if [ "$ubuntu_version" = "20.04" ]; then
    # Copy library for Ubuntu 20.04
    sudo cp -f dependency/libimutils.so /usr/lib
elif [ "$ubuntu_version" = "22.04" ]; then
    # Copy library for Ubuntu 22.04
    sudo cp -f dependency/libimutils.so_for_ubuntu22 /usr/lib/libimutils.so
else
    # Print an error message for unsupported Ubuntu versions
    echo "Error: Unsupported Ubuntu version"
    exit 1
fi

# Copy OpenVino library  
sudo cp -rf dependency/openvino /usr/lib

echo "Installed successfully!"