f=open('file.txt', encoding='utf-8')
text=f.read()
f.close()

print(text)

f=open('file.txt', 'a', encoding='utf-8')
f.write('нова строка\n')
f.close()
#добавляє дані в файл 'a', якщо 'r' для читання, якщо в нас ще немає файла можемо створити 'w'

lines = ['y1','y2']
f=open('file.txt', 'a', encoding='utf-8')
for i in lines:
    f.write(i+ '\n')
f.close()