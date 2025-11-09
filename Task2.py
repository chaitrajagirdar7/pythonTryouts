print("assignment2")
try:
    firstname = input("Pls enter ur firstname :")
    Lastname = input("Pls enter ur lastname :")
except AttributeError as e:
    print("Error message:for input value attempt", e)

print("Hello," + firstname + " " + Lastname + " welcome to the python program")