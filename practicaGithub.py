import os
import subprocess
import time
import webbrowser
#import request
import winreg
git_dir = r"C:\Users\CC6\Desktop\practica3"
repos = [name for name in os.listdir(git_dir)
         if os.path.isdir(os.path.join(git_dir,name)) and
         os.path.exists(os.path.join(git_dir, name, ".git"))]    
if repos:
    print("Found the following github repository in c:\\git.")
    for idx, repo in enumerate(repos, 1):
        print(f"{idx},{repo}")
else:
    print("No github repositories found in C:\\git.")
    print("Please provide a github repository")