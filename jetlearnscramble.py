import random
print("The theme is animals.")
wordslist = ["python","aligator","eagle","clownfish","zebra","deer","lion","canary"]
def scramble(word):
        wordlist = list(word)
        random.shuffle(wordlist)
        return "".join(wordlist)
count = 0
while True:
    word = random.choice(wordslist)
    wordslist.remove(word)
    wordscramble = scramble(word)
    print(wordscramble)
    unscramble = input("What is the word unscrambled? ")
    if unscramble == word:
        print("You got it right!")
        count = count + 1
    else:
        print("You got it wrong :(")
    if not wordslist:
         break
print("You got",count,"out of the 8 right")