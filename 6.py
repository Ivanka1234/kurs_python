my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
palindrome=[]
for word in my_str:
    word_r = word.replace(' ', '').lower()
    if word_r==word_r[::-1]:
        palindrome.append(word)
print(palindrome)

