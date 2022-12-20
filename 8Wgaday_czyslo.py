print('Вгадай число')
c =19
popu=0
czys=0
while True:
    czys= int(input('Введіть число від 1 до 100 '))
    popu +=1
    if czys==c:
        print(f'Ви вгадали загадане число за {popu} спроб')
        break
    elif 100>czys<c:
        print('Ваше число замаленьке')
    elif 100>czys>c:
        print('Ваше число завелике')
    else:
        print('Ви неправильно ввели число')



