import os

input_dir = r"C:\Users\Daniel\Downloads\benyehuda_sep2016_dump_stripped_nikkud_utf8\New folder"
names = []
for subdir, dirs, files in os.walk(input_dir):
    for file in files:
        lastIndexOfBackslach = subdir.rfind('\\')
        name = subdir[lastIndexOfBackslach+1::]
        if not name in names:
            names.append(name)

file = open("names.txt","w+")

for name in names:
    file.write(name)
    file.write("\n")


file.close()


