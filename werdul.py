from random import randrange
from function import funko, rules
import time

for i in range(3):
  print(rules(i))

words = []
length = 0
with open("large.txt", "r") as file:
    while length == 0:
      girth = input("\nHow long da word? ")
      if girth.isnumeric():
        if int(girth) >= 26 or int(girth) <= 0:
          print("Length must be 1 - 25")
        else:
          length = int(girth)
      else:
        print("Invalid Length")
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
        potguess = input("{grid}\n{board}\n{round})Enter Guess: ".format(grid = grid,board=keyboard, round=roundcalc - r))
        if len(potguess) > length:
            print("Guess too long\n")
            time.sleep(0.5)
        elif len(potguess) < length:
            print("Guess too short\n")
            time.sleep(0.5)
        elif potguess not in words:
            print("Guess not in list\n")
            time.sleep(0.5)
        else:
            guess = potguess
        
    
    if length < 10:
      grid += " " * (10 - length)

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


    if guess == answer:
        won = r + 1
        break

message = ""
if won > 0:
  message += "Well Done, you got it in {} guesses".format(won)
else:
  message += "Outta Lives Bitch"

print("{message}, the word was {word}!".format(message=message, word=answer))
