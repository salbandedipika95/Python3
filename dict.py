#python program to generate and print a dictionary that contains a number in th form of (x,x*x)
num=int(input("enter limit:"))
d=dict()
for i in range(1,num+1):
    d[i]=i*i
print(d)
