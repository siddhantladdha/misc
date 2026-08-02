from plumbum.machines import LocalCommand
from plumbum.cmd import gh, chmod
from plumbum import FG
from plumbum.path.utils import delete
from rich import print
import hashlib

def gh_cmd_creator(pkgs: dict[str, dict[str, str]]):
    """Just creates the gh commands in correct format.
    ------
    Parameters:
    pkgs: dict[str, dict[str, str]]
        A dictionary where the key is the package name and the value is a dictionary
        containing the version, pattern, output, and sha256 of the package.
        Usually loaded from a toml file.
    """
    gh_download: list[LocalCommand] = []
    for pkg_name, pkg_info in pkgs.items():
        gh_download.append(
            gh["release",
            "--repo", pkg_name, "download", pkg_info["version"],
            "--clobber",
            "--pattern", str(pkg_info["pattern"]),
            "--output", pkg_info["output"]
            ]
        )
    return gh_download

def cmd_executor(cmds: list[LocalCommand]):
    """Executes the given commands in the foreground.
    Currently, no async since not worth it.
    ------
    Parameters:
    cmds: list[LocalCommand]
        A list of plumbum LocalCommand objects to be executed
    """
    for cmd in cmds:
        # print(cmd)
        # using in FG to see stdout.
        cmd & FG

def checksum_verifier(pkgs: dict[str, dict[str, str]], checksum_algo: str = "sha256"):
    """Verifies the checksum of the downloaded files and makes them executable if they match.
    If the checksum does not match, the file is deleted.
    ------
    Parameters:
    pkgs: dict[str, dict[str, str]]
        A dictionary where the key is the package name and the value is a dictionary
        containing the version, pattern, output, and checksum of the package.
        Usually loaded from a toml file.
    """
    for pkg_name, pkg_info in pkgs.items():
        with open(pkg_info["output"], "rb") as f:
            digest = hashlib.file_digest(f, checksum_algo)
            if digest.hexdigest() == pkg_info["sha256"]:
                print(f"[bold green]{checksum_algo.upper()} matches for "
                    f"{pkg_info["output"]}. "
                    f"Making executable.[/bold green]")
                chmod["u+x", pkg_info["output"]]()
            else:
                print(f"[bold red]{checksum_algo.upper()} mismatch for "
                    f"{pkg_info["output"]}. "
                    f"Deleting file.[/bold red]")
                delete(pkg_info["output"])
