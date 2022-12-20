words = ['мадам', 'топот', 'test', 'madam', 'world']
palindroms=[]
for word in words:
    if word == word[::-1]:
        palindroms.append(word)

print(palindroms)

