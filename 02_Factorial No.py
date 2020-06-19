# Program for printing
# Factorial's

def fac(n):
    if n==0:
        return(1)
    else:
        return(n*fac(n-1)) # Condition for giving factorial value's

inp=int(input())
print("Factorial of",inp,"is:",fac(inp))

'''
Map of the above problem: for n=5

           fun(5)
             /
        n*fun(4)         n=5
           /              ^
      n*fun(3)           n=4
         /                ^
     n*fun(2)            n=3
       /                  ^
    n*fun(1)             n=2
     /                    ^
   n*fun(0)              n=1 
   
   factorial = 1*2*3*4*5 = 120 
'''
