'''Write a Python program to get the Fibonacci series of given range.'''


# for loop with fibonacci series

n=int(input("Enter Value A:"))
a=0
b=1
   
print(a)
print(b)
for i in range(2,n):
 c=a+b
 a=b
 b=c
 print(c)

# while loop with fibonacci series

n=int(input("Enter Value A:"))
a=0
b=1
print(a)
while b<n:
    print(b)
    a,b=b,a+b
print() 
