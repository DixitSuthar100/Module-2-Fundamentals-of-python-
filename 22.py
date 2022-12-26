''' Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
 If the string length is less than 2, return instead of the empty string.'''

string=input("Enter string:")
count=0

# Loop through the string
for i in string:
      count=count+1
new_str=string[0:2]+string[count-2:count]

# Printing the new String
print("string is:")
print(new_str)
