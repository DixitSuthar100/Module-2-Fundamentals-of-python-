''' Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.'''

n1=int(input("Enter Frist Value N1:"))
n2=int(input("Enter Second Value N2:"))
def test(n1,n2):
    if n1==n2 or (n1+n2)==5 or abs(n1-n2)==5:      # abs is convert negative to positive
        return True
    else:
        return False
print(test(n1,n2))



    

