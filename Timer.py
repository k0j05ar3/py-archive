hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))
timer = seconds + (minutes * 60) + (hours * 3600)

import time
import os

while timer >= 0:
  os.system('clear')
  print(timer)
  time.sleep(1)
  timer -= 1
  os.system('clear')

print("Time's up!")