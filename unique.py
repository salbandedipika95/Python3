#python function that takes a list and returns a new list with unique elements of the first list
def unique(L):      #function definition
    a=[]
    for b in L:
        if b not in a:
            a.append(b)
    return a
print(unique([10,2,3,1,2,3,11,4]))      #function call