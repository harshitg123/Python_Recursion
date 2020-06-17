# This program is calculating the 
# whole sum of any no with some addition
# for e.g -> X=5 Y=2 then,
# (x+y)+((x-1)+y)+.......

def fun(X,Y):
    if X==0:
        return Y
    else:
        return(fun(X-1 ,X+Y))

inp1,inp2=int(input()),int(input())
print(fun(inp1,inp2))

# for better understanding visit to geeks for geeks:
# https://www.geeksforgeeks.org/practice-questions-for-recursion/