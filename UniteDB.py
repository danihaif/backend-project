import os

output = open("C:\Users\Daniel\Documents\MIni csv\output.txt","w+")
path = "C:\Users\Daniel\Documents\MIni csv"
for filename in os.listdir(path):
    file_path = filename
    full_path = os.path.join(path,filename)
    with open(full_path,"r") as f:
        for line in f:
            output.write(line)