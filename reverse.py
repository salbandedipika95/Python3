#python program to reverse words in a string
s=input("Enter String:")
w=s.split()           #split the words by default space
for s1 in w:
    for i in range(len(s1)-1,-1,-1):
        print(s1[i],end="")
    print(" ",end="")
