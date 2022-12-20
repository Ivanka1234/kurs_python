import os

tree=os.walk('folder')
for files in tree:
    print(files)