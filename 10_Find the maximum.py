# program to find the maximum
# from list

def fun(a,n):
    if n==1:
        return a[0]
    else:
        x=fun(a,n-1)
    if x>a[n-1]:
        return(x)
    else:
        return a[n-1]

a=[12,10,30,50,100] 
b=len([12,10,30,50,100])
print(fun(a,b))

# for better under standing visit to Geeks for Geeks
# https://www.geeksforgeeks.org/practice-questions-for-recursion-set-4/?ref=lbp