import random 
print("HANGMAN")
wlist = ["galaxy", "asteroid", "satellite", "telescope", "astronaut", "constellation"]
word = random.choice(wlist)
letterlist = ["_"] *len(word)
stages=[
'''
|
|
|
|
|''',

'''
_________
|    
|    
|  
|   
|
''',
'''
_________
|    |
|    
|  
|   
|
''',
'''
_________
|    |
|    O
|  
|   
|
''',
'''
_________
|    |
|    O
|    |
|   
|
''',
'''
_________
|    |
|    O
|   \\|
|   
|
''',
'''
_________
|    |
|    O
|   \\|/
|   
|
''','''
_________
|    |
|    O
|   \\|/
|   /
|
''',
'''
_________
|    |
|    O
|   \\|/
|   / \\
|
''']
countl = 0
while True:
    print( " ".join(letterlist))
    wletter = input("What letter do you think is in the word? ")
    if wletter in word:
        for i in range (len(word)):
            if wletter == word[i]:
                letterlist[i] = wletter 
    else:
        print("Not in the word!")
        countl += 1
        print(stages[countl])


    