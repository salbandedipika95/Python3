#python program to check prime number
flag=0
n=int(input('Enter number'))     #accept number
if n>1:
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
if flag==1:       
    print(n,'is not a prime number')
else:
    print(n,'is a prime number')