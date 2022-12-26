'''Write a Python program to count the number of characters (character frequency) in a string...'''

n=input("Enter String:").lower()        # Take a string as a input from the user.
d={}                                    # Create a empty dictionary
for i in n:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
