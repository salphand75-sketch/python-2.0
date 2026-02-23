import random
print("Welcome to the Word Scramble Game!")
difficulty = input("Choose difficulty (easy / medium / hard): ").lower()

if difficulty == "easy":
print("Theme is: Animals")
wordslist = ["cat", "dog", "lion", "zebra", "deer", "eagle"]

elif difficulty == "medium":
print("Theme is: Countries")
wordslist = ["canada", "brazil", "germany", "india", "france", "japan"]

elif difficulty == "hard":
print("Theme is: Space")
wordslist = ["galaxy", "asteroid", "satellite", "telescope", "astronaut", "constellation"]

else:
print("Invalid choice — defaulting to easy.")
print("Theme is: Animals")
wordslist = ["cat", "dog", "lion", "zebra", "deer", "eagle"]



def scramble(word):
    wordlist = list(word)
    random.shuffle(wordlist)
    return "".join(wordlist)


count = 0
total = len(wordslist)

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

print("You got", count, "out of", total, "right")
