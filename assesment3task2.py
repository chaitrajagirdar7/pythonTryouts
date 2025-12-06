#Write a Python program that:
#1.   Creates a list of numbers from 1 to 10.
#2.   Extracts the first five elements from the list.
#3.   Reverses these extracted elements.
#4.   Prints both the extracted list and the reversed list

numlist=[1,2,3,4,5,6,7,8,9,10]
exlist=[]
revlist=[]
for ele in range(5):
    #print(numlist[ele])
    exlist.append(numlist[ele])
#print("\n Reversing list:")
for i in range(-6, -11, -1):   # -6 → -10
    #print(numlist[i])
    revlist.append(numlist[i])
print("Range specific list:",exlist)
print("Reversed Rangespecific list:",revlist)
