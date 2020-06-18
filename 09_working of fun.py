# program for understanding recursive 
# Function's Working

def fun(n):
    if n>0:
        n-=1
        fun(n)
        print(n,end=" ")
        n-=1
        fun(n)
fun(int(input()))

'''     Working Tree for the above problem:

                   fun(4);
                   /
                fun(3)-> print(3)-> fun(2)(prints 0 1)
               /          ^
           fun(2)-> print(2)-> fun(1)(prints 0)
           /          ^
       fun(1)-> print(1)-> fun(0)(does nothing)
       /          ^            
    fun(0) -> print(0) -> fun(-1) (does nothing)
'''
# for better understanding visit to Geeks for Geeks:
# https://www.geeksforgeeks.org/practice-questions-for-recursion-set-4/?ref=lbp