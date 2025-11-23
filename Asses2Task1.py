# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.
try:
    number=int(input("Enter a number so that i get to evaluate it :"))
    print(f"No. enetered is : {number}")
    if number%2==0 :
      print(f"{number} is even no.")
    elif number%2>0 :
      print(f"{number} is odd no.")
except ValueError:
    print(f"{number} is not a valid number, cannot evaluate for odd/even.")