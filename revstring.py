#python function to reverse a string
s1=input('Enter string: ')
def  reverse_str(s1):         #function definition
    w=s1.split()
    for s1 in reversed(w):
        for i in range(len(s1)-1,-1,-1):
            print(s1[i],end="")
        print(" ",end="")   
reverse_str(s1)          #function call