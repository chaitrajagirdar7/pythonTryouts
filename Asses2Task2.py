# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.
listofnumbers=[]
for i in range(1,51):
  listofnumbers.append(i)
print(f"These are the numbers at listofnumbers:{listofnumbers}")
print(f"This is sum of all numbers of 1-50 : {sum(listofnumbers)}")