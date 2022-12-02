#python function that takes a number as a parameter and check the number is prime or not
n=int(input("Enter Number:"))
def prime(n):          #fuction definition
    f=0
    if n==1:
        f=1
    elif n==2:
        f=0
    else:
        for i in range(2,n):
            if n%i==0:
                f=1
    if f==0:                               
        print("number is prime")
    else:
        print("number is not prime")
    return n
print(prime(n))            #function call
    