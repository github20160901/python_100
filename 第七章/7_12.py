# 修改后缀名
import os  
files = os.listdir(".")
print(files)
for filename in files:
    pos = filename.find(".")
    print(pos)
    if filename[pos + 1:] == "html":
        newname = filename[:pos + 1] + "htm"
        os.rename(filename,newname)
