#python program to remove an item from a tuple
print('original tuple')
tup=(1,'om',3,6,'sai',5,7,8,9)
print(tup)
l=list(tup)
l.remove(3)
t=tuple(l)
print('After removing element')
print(t)
