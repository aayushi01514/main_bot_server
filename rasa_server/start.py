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
    port
]

print(f"Starting Rasa server on port {port}...")
subprocess.run(cmd)
