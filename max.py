#python function to find the max of three numbers
def max(a,b,c):              #function definition
    if a>b and a>c:
        print("a is max=",a)
    elif b>a and b>c:
        print("b is max=",b)
    else:
        print("c is max=",c)
max(11,33,22)              #function call by passing parameters