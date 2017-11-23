import datetime
import time
filename = datetime.datetime.now()
listfiles = ["file1.txt","file2.txt","file3.txt"]

content = ""

for item in listfiles:
    file=open(item,"r")
    text = file.read()
    content = content + text
    file.close()

with open(filename.strftime("%Y-%m-%d")+".txt","w") as file:
        file.write(content)
        print("File has been created")
