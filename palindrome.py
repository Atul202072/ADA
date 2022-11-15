def func(s,low,high,pal):
    while low>=0 and high<len(s) and s[low]==s[high]:
        pal.add(s[low:high+1])
        low=low-1
        high=high+1

def palindromefunc(s):
    pal=set()
    for i in range(len(s)):
        func(s,i,i,pal)
        func(s,i,i+1,pal)
    print(pal)    

str=input("Enter the word: ")
palindromefunc(str)































