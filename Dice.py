import os
import time
import random

print("Welcome to the online dice!")
diceAmount = int(input("How many dice do you want to roll?: "))
sideDice = int(input("How many sides do you want your dice to have?: "))
diceTotal = 0
if diceAmount == 0:
  print("You can't roll 0 dice!")
  exit()
if sideDice == 0:
  print("You can't roll a 0 sided dice!")
  exit()
os.system('clear')

def random_number(sideDice):
  return random.randint(1, sideDice)
diceNumber = random_number(sideDice)

while diceAmount >= 0:
  if diceAmount == 0:
    print("Calculating total...")
    diceAmount -= 1
    time.sleep(5)
    os.system('clear')
  else: 
    diceTotal = diceTotal + diceNumber
    diceAmount -= 1
    print(diceNumber)
    time.sleep(2)
    print("Moving on to next dice...")
    time.sleep(5)
    os.system('clear')
    diceNumber = random_number(sideDice)
  
print("Your total is: " + str(diceTotal))