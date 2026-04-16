# /// script
# dependencies = [
#   "plumbum",
#   "rich",
# ]
# requires-python = ">=3.14"
# ///

from plumbum.cmd import chmod
from plumbum import local
from plumbum.path.utilities import copy, move
from rich import print

build_dir = "python_build"
local.cwd.chdir(build_dir)

print('Extracting appimages.')

appy = ["python", "appimagetool"]
for app in appy:
    app_cmd = local.get("./" + app)
    app_cmd("--appimage-extract")
    move("squashfs-root", app + ".AppDir")

copy("requirements.txt", "python.AppDir")
local.cwd.chdir("python.AppDir")
print('Starting pip install from requirements.txt')
#./usr/bin/pip install -r ./requirements.txt
#./usr/bin/pip freeze --requirement requirements.txt > frozen_requirements.txt
#set -x ARCH x86_64
#cd ..
#./appimagetool.AppDir/AppRun ./python.AppDir python