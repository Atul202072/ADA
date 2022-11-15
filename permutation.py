def permutation(str,answer):
    if len(str)==0:
        print (answer)
        return 
    for i in range(len(str)):
        ch=str[i]
        left=str[0:i]
        right=str[i+1:]
        result=left+right
        permutation(result,answer+ch)

answer=" "
str=input("Enter your string:")
print("All the possible permutations are:")
permutation(str,answer)