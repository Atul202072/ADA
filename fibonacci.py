list=[]
for i in range(25):
    list.append(-1)
print(list)    

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if list[n]!=-1:
        return list[n]

    list[n]=fib(n-1)+fib(n-2)
    return list[n]        

for i in range(5):
    print(fib(i))

print(fib(7))
print(list)


             







