import os
def clear():
    directory = r"C:\cs\tagger.ner\input"
    for path, subdirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(path,filename)
                statinfo = os.stat(str(file_path))
                print (filename)
                print str(statinfo.st_size)
                if statinfo.st_size > 100000:
                    os.remove(file_path)


if __name__ == '__main__':
    clear()