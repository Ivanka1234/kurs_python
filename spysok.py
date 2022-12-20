a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#1 варіант вирішення
for i in a:
    if i<5:
       print(i)

#2 варіант вирішення
print(list(filter(lambda i: i < 5, a)))

#3
print([i for i in a if i < 5])