import os
import subprocess

port = os.getenv("PORT", "5005")

cmd = [
    "rasa",
    "run",
    "--enable-api",
    "--cors",
    "*",
    "--debug",
    "--port",
    f"{port}"   # ensure it’s string
]
print(f"Running command: {' '.join(cmd)}")
subprocess.run(cmd)