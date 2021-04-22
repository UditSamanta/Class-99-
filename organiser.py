import shutil
import os

#path = 'D:\\Python\\Class_99'
path = input('Enter the name of the directory to be sorted')
listOfFiles = os.listdir(path)

for file in listOfFiles:
    name, extension = os.path.splittext(file)
    ext = ext[1:]
    if ext == "":
        continue

    if os.path.exists(path+"/docs"):
        shutil.move(path+"/"+file, path+"/docs/")
    else:
        os.mkdir(path+"/docs")
        shutil.move(path+"/"+file, path+"/docs/")