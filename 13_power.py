# program for calculating 
# power i.e a^b of two no.

def mul(a,b):
    if b==0:
        return 1
    if b%2==0:
        return mul(a*a, b//2)
    else:
        return a*mul(a*a, b//2)
        
print(mul(int(input()),int(input())))        

# for better understand visit Geeks for Geeks
# https://www.geeksforgeeks.org/practice-questions-for-recursion-set-5/?ref=lbp