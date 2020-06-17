# Program is for printing 
# A Triangle

# *  *  *  *  * . . .
# *  *  *  * 
# *  *  * 
# *  * 
# *  

def  fun1(n): 
    if (n <= 0):
        return
    else:
        for i in range(n): 
            print(" * ",end="")
        print("\n",end="")
        fun1(n - 1) 
fun1(int(input()))        

# I modified this question for printing 
# Triangle but for you want a look then visit 
# Geeks for Geeks :- https://www.geeksforgeeks.org/practice-questions-for-recursion-set-3/?ref=lbp