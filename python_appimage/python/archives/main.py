import tomllib
from pacman import gh_cmd_creator, cmd_executor, checksum_verifier
from plumbum import local
from plumbum.path.utils import copy, delete
from plumbum.machines import LocalCommand
from rich.traceback import install
install(show_locals=True)

def main():
    print(f"CWD:{local.cwd}")
    build_dir = "build"
    delete(build_dir)
    local.cwd.mkdir(build_dir)
    copy([
    "pacman.toml",
    "appimage_build.py",
    "requirements.txt"],
    build_dir)
    with local.cwd(build_dir):
        print(f"CWD:{local.cwd}")
        with open("pacman.toml", "rb") as f:
            pkgs = tomllib.load(f)

        gh_download: list[LocalCommand] = gh_cmd_creator(pkgs)
        cmd_executor(gh_download)
        checksum_verifier(pkgs)

if __name__ == "__main__":
    main()
