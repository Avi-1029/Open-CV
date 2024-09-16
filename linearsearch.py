fruits = ['Banana','Orange','Dragonfruit','Papaya','Apple']
item = input('What does thou want to search for?')
found = False
for f in fruits:
    if item == f:
        print('YES!! Your fruit is in my list')
        found = True
        break

#else:
#    print('NO, your fruit isnt worthy enough to be on my list.')

if found == False:
    print('NO, your fruit isnt worthy enough to be on my list.')