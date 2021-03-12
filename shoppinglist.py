# Shopping List v 0.2

print('Shopping list:')
print('\"I need you to buy this at the store! Please, take in count the following instructions\"')
print('If you find eggs, buy 10')
print('If you find butter bars, buy 2')
print('If yoy find BOTH eggs and butter, buy 4 of each INSTEAD')
print('If you find pies... well, forget the eggs and butter, and bring 2 pies! :)')
print('~    ~   ~   ~   ~   ~   ~   ~')
print('IMPORTANT: Use \'y\' (YES) and \'n\' (NO) to check the list!')
print('#    #   #   #   #   #   #   #   #   #')

eggsE = input(str(('Now, here at the store, are there eggs available? (y/n) ')))

if eggsE == 'y':        # The 'E' is for 'existence' (in stock)
    print('Great! I found the eggs and picked 10 of them')
    eggsQ = int(10)     # And the 'Q' for 'quantity'
    eggsE = True
elif eggsE == 'n':
    print('Oh... it looks there are no eggs left.')
    eggsQ = int(0)
    eggsE = False
else:
    print()

butterE = input(str(('Now, are there butter bars available? (y/n) ')))

if butterE == 'y' and eggsE == True:
    print('Nice! I found the butter bars!')
    print('Since I found BOTH the eggs and butter, I will take 4 of each (since the lists says so)')
    eggsQ = int(4)
    butterQ = int(4)
    butterE = True
elif butterE == 'y' and eggsE == False:
    print('Good, I found the butter bars.')
    print('But I didn\'t find any eggs.')
    butterQ = int(2)
    butterE = True
elif butterE == 'n' and eggsE == True:
    print('Oh... there are no butter bars left. At least I found the eggs!')
    butterQ = int(0)
    butterE == False
elif butterE == 'n' and eggsE == False:
    print('Gosh... I didn\'t find NEITHER the eggs or the butter!')
    print('That\'s so unlucky..')
    butterQ = int(0)
    butterE == False
else:
    print()

piesE = input(str(('Finally... are there any pies left in the shop? (y/n) ')))

if piesE == 'y':
    print('Yes! There are! As the list say, I will take 2 pies and LEAVE the eggs and the butter')
    piesQ = int(2)
    piesE = True
elif piesE == 'n':
    print('I see, there are NO pies left.')
    piesQ = int(0)
    piesE = False
else:
    print()

print('- At home -')
print('Well this is what I brought from the store:')

if eggsE == True and butterE == True and piesE == False:
    print(f'Since I found BOTH the eggs and butter, I bought {eggsQ} eggs and {butterQ} butter bars')
    print(f'I found {piesQ} pies at the store')
elif eggsE == True and butterE == False and piesE == False:
    print(f'I got {eggsQ} eggs at the store, but didn\'t find neither the butter bars {butterQ} or the pies {piesQ}')
elif eggsE == False and butterE == True and piesE == False:
    print(print(f'I got {butterQ} butter bars at the store, but didn\'t find neither the eggs {eggsQ} or the pies {piesQ}'))
elif eggsE == False and butterE == False and piesE == False:
    print(f'Apologies.. I dind\'t find NEITHER the eggs {eggsQ}, the butter bars {butterQ} or the pies {piesQ}')
elif eggsE == True or eggsE == False and  butterE == True or butterE == False and piesE == True:
    print(f'Well, since I found the pies you asked for, I bought {piesQ} of them!')
    print(f'At the store, I found {eggsQ} egg(s) and {butterQ} butter bar(s), but LEFT those')
else:
    print()

print('~    ~   ~   ~   ~   ~   ~   ~')
