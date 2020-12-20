#a4_p2

ch= input('Enter an uppercase character please: ')
n= int(input("Enter an integer please : "))
asc=ord(ch)
for index in range(n+1):
    print(chr(asc+index),end=' ')
print()



