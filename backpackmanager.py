import os

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
print(current_dir)

import yaml
import algorithm
import win32com.client

with open("shortcut.yaml") as file:
    data = yaml.safe_load(file)

create_chortcut = data["shortcut"]

exe_path = os.path.join(current_dir, "backpackmanager.exe")
yaml_path = os.path.join(current_dir, "schedule.yaml")

import shutil

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
if not os.path.exists(desktop_path):
    desktop_path = os.path.join(shutil.os.environ["USERPROFILE"], "Desktop")

yaml_shortcut_target_path = os.path.join(desktop_path, "schedule.lnk")
exe_shortcut_target_path = os.path.join(desktop_path, "backpackmanager.lnk")

shortcut_path = os.path.join(current_dir, "shortcut.yaml")



if create_chortcut["sh"]:
    if input("Create desktop shortcut? Y/N").lower() == "y":
        shell = win32com.client.Dispatch("WScript.Shell")

        shortcutexe = shell.CreateShortCut(exe_shortcut_target_path)
        shortcutexe.Targetpath = exe_path
        shortcutexe.WorkingDirectory = current_dir
        shortcutexe.save()

        shortcutyaml = shell.CreateShortCut(yaml_shortcut_target_path)
        shortcutyaml.Targetpath = yaml_path
        shortcutyaml.WorkingDirectory = current_dir
        shortcutyaml.save()

        yaml.safe_dump({"shortcut": {"sh": False}}, open(shortcut_path, "w"))
        print("Shortcut created.")


output = algorithm.find_best_config()

print(f"\nOptimal configuration: {output}")
print("Not what you wanted? Check README.txt")

input("\nPress any key to exit")