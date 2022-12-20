import random

c = 0
b = random.randint(1, 10)
while True:
    y=input('zigrajete?')
    v=('tak')
    if y==v:
        while True:
            a = int(input('wpuszit czyslo '))
            c +=1
            if a == b:
                print(f'vhadaw za {c} sprob, wasze czyslo {b}')
                break
            elif a > b:
                print('zawelyke')
            else:
                print('zamale')
    else:
        print('dakuy za igry')
        break