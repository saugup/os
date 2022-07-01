import os
import shutil 
import time

cwd = os.getcwd()
print("current woring directory:",cwd)

path = input("enter a folder path to remove")
isExist = os.path.exists(path)

print("path exists = ", isExist)
os.rmdir(path)
print("removed successfully")

if isExist:
    dir_list = os.listdir(path)
    print("files and directories in ", path)
    print(dir_list)
    for (root,dirs,files) in os.walk(path):
        print("root = ",root)
        print("folder = ", dirs)
        print("file name = ",files)
else:
    print("incorrect path")

