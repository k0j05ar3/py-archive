import os
import random
import time

playAgain = True #keeps the loop going
userScore = 0 #keeps track of the user's score
cpuScore = 0 #keeps track of the cpu's score
playOptions = ["Rock", "Paper", "Scissors"] # allows the computer to choose what to play

#Beginning of the game
print("Welcome to Rock, Paper, Scissors!")
time.sleep(3)

while playAgain: # start of the loop
  os.system('clear')
  userChoice = input("Choose Rock, Paper, or Scissors: ")
  if userChoice != "Rock" and userChoice != "Paper" and userChoice != "Scissors":
    os.system('clear')
    print("Please enter a valid option")
    exit()
  cpuChoice = random.choice(playOptions) # computer chooses an option
  print("Rock...")
  time.sleep(1)
  print("Paper...")
  time.sleep(1)                     #building excitement
  print("Scissors...")
  time.sleep(1)
  print("Shoot!")
  time.sleep(1)
  os.system('clear')
  print("The player chose to play: " + userChoice)
  print("The computer chose to play: " + cpuChoice)
  #-----------------
  
  if userChoice == cpuChoice:
    print("It's a tie!")
  elif userChoice == "Paper" and cpuChoice == "Rock":
    print("You win!")
    userScore += 1
  elif userChoice == "Scissors" and cpuChoice == "Paper":
    print("You win!")
    userScore += 1
  elif userChoice == "Rock" and cpuChoice == "Scissors":
    print("You win!")
    userScore += 1
  else:
    print("You lose!")
    cpuScore += 1

  playAgain = input("Would you like to play again? (y/n): ")
  if playAgain == "y":
    playAgain = True
  else: 
    playAgain = False
    os.system('clear')
    print("Your score: " + str(userScore))
    print("Computer score: " + str(cpuScore))
    if userScore > cpuScore:
      print("You win!")
    elif cpuScore > userScore:
      print("You lose!")
    else:
      print("It's a tie!")