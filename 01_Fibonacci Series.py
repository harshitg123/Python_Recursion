# Program for printing n no. of
# Fibonacci Series

def fab(n): 
    if n==0: # returning zero if n is equal to 0
        return(0)
    if n==1 or n==2: # returning one if n is equal to 1 or 2 
        return(1)
    else:
        return(fab(n-1)+fab(n-2)) # the main condition for printing whole Series

inp=int(input())
print("Fibonacci Series of",inp,"is:",end=" ")
for i in range(0,inp):
    print(fab(i),end=" ") # Calling fab function for each value in range from 0 to the range user inputed
    
  
