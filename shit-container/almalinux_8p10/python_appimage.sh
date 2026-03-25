#!/bin/bash
wget https://github.com/niess/python-appimage/releases/download/python3.14/python3.14.0-cp314-cp314-manylinux2014_x86_64.AppImage
wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
chmod +x python3.14.0-cp314-cp314-manylinux2014_x86_64.AppImage
chmod u+x appimagetool-x86_64.AppImage
./python3.14.0-cp314-cp314-manylinux2014_x86_64.AppImage --appimage-extract
mv squashfs-root python3.14.0-cp314-cp314-manylinux2014_x86_64.AppDir
./appimagetool-x86_64.AppImage --appimage-extract
mv squashfs-root appimagetool-x86_64.AppDir
cd python3.14.0-cp314-cp314-manylinux2014_x86_64.AppDir/
./usr/bin/pip install pydantic scipy sympy numpy pandas polars ruff hypothesis rich xarray boltons icecream toolz marimo
python3.14.0-cp314-cp314-manylinux2014_x86_64.AppDir/AppRun -m pip list
ARCH=x86_64 ./appimagetool-x86_64.AppDir/AppRun python3.14.0-cp314-cp314-manylinux2014_x86_64.AppDir python3.14.0-cp314-cp314-manylinux2014_x86_64_custom.AppImage
