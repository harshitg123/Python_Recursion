# Program for printing
# Factorial's

def fac(n):
    if n==0:
        return(1)
    else:
        return(n*fac(n-1)) # Condition for giving factorial value's

inp=int(input())
print("Factorial of",inp,"is:",fac(inp))
