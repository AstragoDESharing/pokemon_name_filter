import subprocess
import sys


def generate_requirements():
    subprocess.run(["poetry", "export", "-f", "requirements.txt",
                   "-o", "requirements.txt", "--without-hashes"], shell=True)


if __name__ == "__main__":
    generate_requirements()
