#python function to check whether a number is perfect or not
n=int(input("Enter Number:"))
def perfect(n):              #function definition
    s=0
    for i in range(1,n):
        if (n%i)==0:
            s=s+i
            i+1
    if n==s:
        print("number is perfect")
    else:
        print("number is not perfect") 
print(perfect(n))           #function call