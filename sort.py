#python program o sort dictionary in ascending or descending order
d1={1:"om",2:"sai",3:"ram"}
s=sorted(d1.values())
print("Ascending order list=",s)
s2=sorted(d1.values(),reverse=True)
print("Descending order list=",s2)
