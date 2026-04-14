#!/usr/bin/env fish
set tmpdir (mktemp -d -p .)
cp ./requirements.txt $tmpdir/
cd $tmpdir
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
