import os
import glob
import shutil

files = glob.glob("*")
print(files)

extensions = set()

for file in files:
    extension = file.split(sep=".")
    
    try:
        extensions.add(extension[1])
    except IndexError:
        continue


def creatDir():
    for dir in extensions:
        try:
            os.makedirs(dir+"_files")
        except FileExistsError:
            continue

def arrang():
    for file in files:
        exexf = file.split(sep = ".")
        try:
            shutil.move(file, exexf[1]+"_files/")
        except (OSError, IndexError):
            continue

creatDir()
arrang()

