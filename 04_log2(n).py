# this is calculating 
# log2(n)

def fun(N):
    if N<=1:
        return(0)
    else:
        return(1+fun(N//2))

inp=int(input())
print(fun(inp))

# for further understanding visit geeks for geeks
# https://www.geeksforgeeks.org/practice-questions-for-recursion-set-2/?ref=lbp