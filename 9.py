'''Write a Python program to sum of three given integers. However, if two values are equal sum will be zero'''

n1=int(input("Enter Frist Value N1:"))
n2=int(input("Enter Second Value N2:"))
n3=int(input("Enter Third Value N3:"))
if n1==n2 or n2==n3 or n1==n3:
    print("Sum is:",0)
else:
    print("Sum is:",n1+n2+n3)
    


'''Sum of N Number....'''

n=int(input("Enter N:"))
Sum=0
while n>0:
    Sum=Sum+n
    n=n-1
    print("Sum:",Sum)
