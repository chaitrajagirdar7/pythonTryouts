print(" Assignment1 \n =================")
num = []
for i in range(2):
    try:
      number=input("Enter a num"+str(i+1)+":")
      num.append(number)
    except AttributeError as e:
        print("Error message:for input value attempt"+i+1, e)
for i in range(2):
    #print((num[i]))
  print("Adding numbers u entered & sum is :",int(num[i])+int(num[i+1]))
  print("Subtracting numbers u entered & Number is :",int(num[i])-int(num[i+1]))
  print("Multiplying numbers u entered & Number is :",int(num[i])*int(num[i+1]))
  print("Dividing numbers u entered & Result is :",int(num[i])/int(num[i+1]))
  break