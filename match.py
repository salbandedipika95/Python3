#python program to count the number of matching characters in a pair of string
s1= input(" String1:")
s2= input("String2:")
a=set([])
for ch in s1:
    if ch in s2:
        a.add(ch)
print("Number of match char=",len(a))