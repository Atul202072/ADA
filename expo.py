def power(a,b):
    if (b==0):
        return 1
    elif (b%2==0):
        x=power(a,b/2)
        x=x*x
    else:
        x=power(a,(b-1)/2)
        x=a*x*x
    return x    
    
print(power(5,55555555555))    