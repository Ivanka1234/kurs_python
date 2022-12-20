import zipfile
import os

folder_path= 'c:\\Users\\Аk_47\\PycharmProjects\\pythonProject1\\folder'
zip_path= 'c:\\Users\\Аk_47\\PycharmProjects\\pythonProject1\\folder\\test.zip'
zip_name='test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')
#my_zip.write('c:\\Users\\Аk_47\\PycharmProjects\\pythonProject1\\folder\\1.txt', compress_type=zipfile.ZIP_DEFLATED, arcname='new.txt')

for folder, supfolders, files in os.walk(folder_path):
    #print(folder, files)
    for file in files:
        if file==zip_name:
            continue #щоб удалити наш архів test.zip
        my_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), folder_path), compress_type=zipfile.ZIP_DEFLATED)

my_zip.close()