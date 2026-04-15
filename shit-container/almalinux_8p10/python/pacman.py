# /// script
# dependencies = [
#   "plumbum",
#   "rich",
# ]
# requires-python = ">=3.14"
# ///

from plumbum.cmd import gh, chmod, rm, cp, mkdir
from plumbum import FG
from plumbum import local
from plumbum.path.utils import copy
import tomllib
from rich import print
import hashlib

mkdir("python_build")
copy([
"./pacman.toml",
"./requirements.txt"],
"python_build")
local.cwd.chdir("python_build")

with open("pacman.toml", "rb") as f:
    pkgs = tomllib.load(f)

# Use gh since it is available in github actions runner.
gh_download = []
for pkg_name, pkg_info in pkgs.items():
    gh_download.append(
        gh["release",
           "--repo", pkg_name, "download", pkg_info["version"],
           "--clobber",
           "--pattern", str(pkg_info["pattern"]),
           "--output", pkg_info["output"]
        ]
    )

for cmd in gh_download:
    # print(cmd)
    # no async since not worth it.
    # using in FG to see stdout.
    cmd & FG

for pkg_name, pkg_info in pkgs.items():
    with open(pkg_info["output"], "rb") as f:
        digest = hashlib.file_digest(f, "sha256")
        if digest.hexdigest() == pkg_info["sha256"]:
            print(f"[bold green]SHA256 matches for "
                  f"{pkg_info["output"]}. "
                  f"Making executable.[/bold green]")
            chmod["u+x", pkg_info["output"]]()
        else:
            print(f"[bold red]SHA256 mismatch for "
                  f"{pkg_info["output"]}. "
                  f"Deleting file.[/bold red]")
            rm[pkg_info["output"]]()
