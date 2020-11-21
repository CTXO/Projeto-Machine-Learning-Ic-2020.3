import os, shutil
os.chdir("../imagens")


index = 1
for dir in os.listdir():
    for pic in os.listdir(dir):
        if len(str(index)) == 1:
            shutil.move(f"{dir}/{pic}", "0" + str(index))
        else:
            shutil.move(f"{dir}/{pic}", str(index))
