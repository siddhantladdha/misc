#!/usr/bin/env fish
set tmpdir (mktemp -d -p .)
cp ./requirements.txt $tmpdir/
cd $tmpdir
# Use gh since it is available in github actions runner.
gh release --repo niess/python-appimage \
    download \
    python3.14 \
    --pattern "*cp314-manylinux2014_x86_64.AppImage" \
    --output python
echo 05b6cf8418118c20df6e16cb7fac38e137daf73be9d16aec13328b260d79c407 \
    ./python | sha256sum --check
chmod u+x python

gh release --repo AppImage/appimagetool \
    download \
    continuous \
    --pattern "*x86_64.AppImage" \
    --output appimagetool
echo a6d71e2b6cd66f8e8d16c37ad164658985e0cf5fcaa950c90a482890cb9d13e0 \
    ./appimagetool | sha256sum --check
chmod u+x appimagetool

echo 'Extracting appimages.'
./python --appimage-extract
mv squashfs-root python.AppDir
./appimagetool --appimage-extract
mv squashfs-root appimagetool.AppDir

cp ./requirements.txt python.AppDir/
cd python.AppDir
echo 'Starting pip install from requirements.txt'
./usr/bin/pip install -r ./requirements.txt
./usr/bin/pip freeze --requirement requirements.txt > frozen_requirements.txt
set -x ARCH x86_64
cd ..
./appimagetool.AppDir/AppRun ./python.AppDir python
