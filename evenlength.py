#python program to print even length words in a string
s=input("Enter String:")
w=s.split()
print("word in even length")
for s1 in w:
    if(len(s1)%2==0):
        print(s1,end=" ")