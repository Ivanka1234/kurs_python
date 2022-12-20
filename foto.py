
import os, time
import datetime
import piexif
import shutil


foto_direct= 'C:\\Users\\Аk_47\\PycharmProjects\\pythonProject1\\foto'
files=os.listdir(foto_direct)
files2= filter(lambda x: x.endawith('.jpg') or x.endawith('.JPG'), files)
os.chdir(foto_direct)

def d():
    for x in range (1,13):
        if x>9:
            if not os.path.exists(str(x)):
                os.makedirs(str(x))
        else:
            if not os.path.exists('0'+str(x)):
                os.makedirs('0'+str(x))

def mod_date(file):
    t = os.path.getmtime(file)
    return datetime.datetime.fromtimestamp(t)

a=[] #['AAE', 'MOV', 'JPG', 'PNG']
for root, dirs, files in os.walk(foto_direct):
    for file in files:
        if file[-3:] not in a:
            a.append(file[-3:])
        if file[-3:] in a:
            year=str(mod_date(file))[:10][:4]
            if not os.path.exists(year):
                os.makedirs(year)
            os.chdir(foto_direct+'/'+year)
            d()
            os.chdir(foto_direct)

try:
    for root, dirs, files in os.walk(foto_direct):
        for file in files:
                if file[-3:] in a:
                    year=str(mod_date(file))[:10][:4]
                    month=str(mod_date(file))[:10][5:7] #месяц создания фото
                    shutil.move(file, year+'/'+month+'/'+file) #перенос файла в папку
except EnvironmentError:
    ('Вроде готово')