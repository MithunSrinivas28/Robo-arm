# robotic-arm/setup.sh
#!/bin/bash
# Update package lists
sudo apt-get update
# Install Python3 dev and audio dependencies
sudo apt-get install -y python3-pip python3-dev portaudio19-dev libportaudio2 libatlas-base-dev
# Install pip packages from requirements
pip3 install -r requirements.txt
