#python program to remove i^th character from string 
s=input("Enter String:")
i=int(input("Enter ith position:"))
s1=s[0:i]+s[i+1:]
print("After Removing ith character=",s1)