names= ['Ryan', 'Kieran', 'Mark', 'John', 'David', 'Paul']
for_names=[]
for name in names:
    if name == name[:4:]:
        for_names.append(name)

print(for_names)