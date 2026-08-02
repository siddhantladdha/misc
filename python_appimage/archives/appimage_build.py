# /// script
# dependencies = [
#   "plumbum",
#   "rich",
# ]
# requires-python = ">=3.14"
# ///

from plumbum import local, FG
from plumbum.path.utils import copy, move
from rich import print
from rich.traceback import install
install(show_locals=True)

print('Extracting appimages.')

appy: list[str] = ["python", "appimagetool"]
for app in appy:
    app_cmd = local.get("./" + app)
    app_cmd("--appimage-extract")
    move("squashfs-root", app + ".AppDir")

copy("requirements.txt", "python.AppDir")
with local.cwd("python.AppDir"):
    print('Starting pip install')
    pip = local.get("./usr/bin/pip")
    pip("install", "-r", "requirements.txt") # & FG
    print('Finished pip install')
    print('Starting pip freeze')
    (pip["freeze", "--requirement", "requirements.txt"] > "frozen_requirements.txt") #& FG
    print('Finished pip freeze')

local.env["ARCH"] = "x86_64"
apptool = local.get("./appimagetool.AppDir/AppRun")
print('Started appimage creation.')
# appimagecli gives a warning which gives us a traceback
apptool("./python.AppDir", "python_custom", retcode = None)
print('Finished creating python appimage.')
