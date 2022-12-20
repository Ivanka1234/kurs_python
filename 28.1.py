
def find_sum(n):
    rezult = 0
    for n in range(n+1):
        if n % 5 ==0 or n % 3 ==0:
            rezult +=n
    return rezult
print(find_sum(5))

