#python program to check armstrong number
n=int(input('Enter number'))
s=0
n1=n
while n>0:
    d=n%10
    s=s+(d*d*d)
    n=n//10
if s==n1:
    print('Number is armstrong')
else:
    print('Number is not armstrong')