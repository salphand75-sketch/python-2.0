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
countw = 0
used_letters = []
while True:
    print( " ".join(letterlist))
    wletter = input("What letter do you think is in the word? ")
    if wletter in used_letters:
        print("You already used that letter!")
        continue
    if len(wletter) != 1:
        print("Please enter only ONE letter.")
        continue
    used_letters.append(wletter)
    if wletter in word:
        for i in range (len(word)):
            if wletter == word[i]:
                letterlist[i] = wletter 
                countw += 1
        if "_" not in letterlist:
            print(" ".join(letterlist))
            print("You win.")
            break
    else:
        print("Not in the word!")
        print(stages[countl])
        countl += 1
        if countl == len(stages):
            print("You lose")
            print("The word was:", word)
            break    