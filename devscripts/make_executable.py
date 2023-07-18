import subprocess
import sys


def make_executable():
    subprocess.call(["poetry", "run", "pyinstaller",
                    "--noconfirm", "--onefile", "--console", "--distpath", "./build", "./src/main.py"], shell=True)


if __name__ == "__main__":
    make_executable()
