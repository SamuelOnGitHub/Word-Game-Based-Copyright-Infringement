from random import randrange
from function import funko, duplicate


words = []
length = 0
with open("large.txt", "r") as file:
    length = int(input("How long da word? "))
    wholefile = file.read().split()
    for w in wholefile:
        if len(w) == length and w.isalpha():
            words.append(w)



answer = words[randrange(0, len(words))]

alphabet = "qwertyuiopasdfghjklzxcvbnm"
alphabettrue = "qwertyuiopasdfghjklzxcvbnm"

letters = {}
for i in alphabet:
    letters[i] = funko(i)

grid = "\n"
  
won = 0
roundcalc = 6 + abs(5 - length)
for r in range(roundcalc):
    guess = "" 
    keyboard = alphabettrue[:10] + "\n" + alphabettrue[10:19] + "\n " + alphabettrue[19:]
    temp = ""
    for c in keyboard:
      temp += (c + " ").upper()
    keyboard = temp
    for c in keyboard:
      while guess == "":
        potguess = input("\n{board}\n{round})Enter Guess: ".format(board=keyboard, round=roundcalc - r))
        if len(potguess) > length:
            print("Guess too long\n")
        elif len(potguess) < length:
            print("Guess too short\n")
        elif potguess not in words:
            print("Guess not in list\n")
        else:
            guess = potguess


    for c in range(0,len(guess)):
        if guess[c] not in answer:
            alphabettrue = alphabettrue.replace(guess[c], letters[guess[c]][2])
            grid += funko(guess[c])[2]
        if guess[c] in answer:
            if guess[c] == answer[c]:
              alphabettrue = alphabettrue.replace(guess[c], letters[guess[c]][0])
              grid += funko(guess[c])[0]
            else:
              alphabettrue = alphabettrue.replace(guess[c], letters[guess[c]][1])
              grid += funko(guess[c])[1]

        grid += " "
    grid += "\n"
    print(grid)

    if guess == answer:
        won = 1
        break

message = ""
if won == 1:
  message += "Well Done"
else:
  message += "Outta Lives Bitch"

print("{message}, the word was {word}!".format(message=message, word=answer))


