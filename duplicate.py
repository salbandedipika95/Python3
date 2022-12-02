#python program to remove duplicates from a list
L=[5,7,2,6,5,2,7,5]
a=[]
for b in L:
    if b not in a:
        a.append(b)
print(a)
