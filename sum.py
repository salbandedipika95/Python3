#python function to sum all the numbers in a list
def sum(list):     #function definition
    s=0
    for i in list:
        s=s+i
        i+1
    print("sum of list item=",s)     #print sum of all numbers
sum([20,5,1,4])        #function call