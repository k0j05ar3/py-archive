import time
import os

operS = input("Enter operation: +, -, *, /: ")

if operS == "+":
  num1 = input("Enter first number: ")
  num2 = input("Enter second number: ")
  print("Calculating...")
  time.sleep(1)
  print("The answer is " + str(int(num1) + int(num2)))
elif operS == "-":
  num1 = input("Enter first number: ")
  num2 = input("Enter second number: ")
  print("Calculating...")
  time.sleep(1)
  print("The answer is " + str(int(num1) - int(num2)))
elif operS == "*":
  num1 = input("Enter first number: ")
  num2 = input("Enter second number: ")
  print("Calculating...")
  time.sleep(1)
  print("The answer is " + str(int(num1) * int(num2)))
elif operS == "/":
  num1 = input("Enter first number: ")
  num2 = input("Enter second number: ")
  print("Calculating...")
  time.sleep(1)
  print("The answer is " + str(int(num1) / int(num2)))
else:
  print("Invalid operation")