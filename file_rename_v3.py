#!/usr/bin/env python3
import os                  
BLACK = "\033[40m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
os.system('clear')
print(BLACK + CYAN + "=== 13C Auto Rename V3 ===" + RESET)
path = "/sdcard/Download"  # str applied
count = 1  # int applied
print(BLACK + YELLOW + f"Renaming files in: {path}" + RESET)

if not os.path.exists(path):
    print(BLACK + "Folder not found!" + RESET)
    exit()

for filename in os.listdir(path):
    if "." in filename:
        ext = filename.split(".")[-1]  # str: get extension
        old_path = path + "/" + filename  # str: full old path
        
        # int + str combo: "13C_File_" + "1" + ".jpg"
        new_name = "13C_File_" + str(count) + "." + ext  # str + int + str
        new_path = path + "/" + new_name  # str: full new path
        
        os.rename(old_path, new_path)  # Rename it
        
        print(BLACK + GREEN + f"Renamed: {filename} -> {new_name}" + RESET)
        count = count + 1  # int math: 1, 2, 3...

print(BLACK + CYAN + f"\n=== Done. Renamed {count-1} files ===" + RESET)
print(BLACK + YELLOW + "int counter + str name = Automation" + RESET)
print(BLACK + GREEN + "[+] Sem 2 Pass = Buy ROG 3 CASH" + RESET)
print(BLACK + RESET)
