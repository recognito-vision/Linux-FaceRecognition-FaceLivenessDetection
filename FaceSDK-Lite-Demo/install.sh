#!/bin/sh

echo "Install environment..."

. /etc/os-release
ubuntu_version="$VERSION_ID"
echo "Ubuntu version: $ubuntu_version"

# Install packages:
sudo apt-get update -y && sudo apt-get install -y python3 python3-pip python3-opencv libcurl4-openssl-dev libssl-dev libtbb-dev

# Install requirements:
python3 -m pip install --upgrade pip && python3 -m pip install opencv-python flask flask-cors gradio waitress

echo "Installed successfully!"