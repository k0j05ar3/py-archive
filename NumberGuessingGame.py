import random
import time
import os
# imports for functions

incorrectGuesses = []
incorrectGuess = 0
hint = False

def choose_random_number():
  # Generate a random number between 1 and 100
  return random.randint(1, 100)
randomNumber = choose_random_number()
# computer chooses a number

if 1 < randomNumber < 10:
  hint = ("The number is between 1 and 10")
elif 10 < randomNumber < 20:
  hint = ("The number is between 10 and 20")
elif 20 < randomNumber < 30:
  hint = ("The number is between 20 and 30")
elif 30 < randomNumber < 40:
  hint = ("The number is between 30 and 40")
elif 40 < randomNumber < 50:
  hint = ("The number is between 40 and 50")
elif 50 < randomNumber < 60:
  hint = ("The number is between 50 and 60")
elif 60 < randomNumber < 70:
  hint = ("The number is between 60 and 70")
elif 70 < randomNumber < 80:
  hint = ("The number is between 70 and 80")
elif 80 < randomNumber < 90:
  hint = ("The number is between 80 and 90")
elif 90 < randomNumber < 100:
  hint = ("The number is between 90 and 100")
else:
  print("Computer broke. Restart the program." + "\n" + "Error code: 001")

print("Welcome to the Number Guessing Game!")  # welcoming the user
userGuess = int(input("Guess a number between 1 and 100: "))#allows the user to guess a number

while userGuess != randomNumber:
  if userGuess in incorrectGuesses:
    os.system('clear')
    incorrectGuess = incorrectGuess + 1
    print("You aleady guessed that number! Try again.")
    if incorrectGuess >= 7:
      print(hint)
    userGuess = int(input("Guess a number between 1 and 100: "))
  elif userGuess < randomNumber:
    os.system('clear')
    incorrectGuess = incorrectGuess + 1
    incorrectGuesses.append(userGuess)
    print("Too low! Try again.")
    if incorrectGuess >= 7:
      print(hint)
    userGuess = int(input("Guess a number between 1 and 100: "))
    if incorrectGuess >= 7:
      print(hint)
      if incorrectGuess >= 7:
        print(hint)
  elif userGuess > randomNumber:
    os.system('clear')
    incorrectGuess = incorrectGuess + 1
    incorrectGuesses.append(userGuess)
    print("Too high! Try again.")
    if incorrectGuess >= 7:
      print(hint)
    userGuess = int(input("Guess a number between 1 and 100: "))

os.system('clear')
print("You did it! The number was", randomNumber)
print("Your incorrect attempts: ", incorrectGuess)
print("Your incorrect guesses: ", incorrectGuesses)