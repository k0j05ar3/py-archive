import random
import time
import os
os.system('cls')

guessTrial = list(range(1, 101))
print("Welcome to the Number Guessing Game! \n Instead of you guessing the number... I will try to guess the number you are thinking of.")
time.sleep(3)
userNumber = int(input("Please input the number you are thinking of! \n I promise I won't cheat:"))
if userNumber not in guessTrial:
    print("I can't guess that bruh")
    exit()

guesses = []
tries = 0
guessed = False
cpuGuess = 0
os.system('cls')

while guessed == False:
    cpuGuess = random.choice(guessTrial)
    guesses.append(cpuGuess)
    tries += 1
    if cpuGuess == userNumber:
        os.system('cls')
        print("I guessed your number:", cpuGuess)
        time.sleep(2)
        print("Here are my stats:")
        time.sleep(1)
        print("Tries:", tries)
        time.sleep(1)
        print("Guesses:", guesses)
        time.sleep(1)
        guessed = True
    else:
        print(cpuGuess, "... That wasn't your number.")
        guessTrial.remove(cpuGuess)
        time.sleep(2)
        
