#!/bin/sh
mkdir -p /tmp/build
cd /tmp/build
git clone --depth 1 https://github.com/xonsh/xonsh
cd xonsh/appimage
echo 'xonsh' > requirements.txt
cat pre-requirements.txt >> requirements.txt  # here you can add your additional PyPi packages to pack them into AppImage
cd ..
pip install git+https://github.com/niess/python-appimage
python -m python_appimage build app -p 3.11 ./appimage