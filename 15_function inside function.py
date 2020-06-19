# This program is to understand
# function inside a function i.e fun(fun(fun(n)))

def fun(count):
    print(count)
    if count<3:
        count+=1
        fun(fun(fun(count)))
    return count
if __name__ == "__main__":
    fun(int(input()))        
# visit to Geeks for Geeks 
# https://www.geeksforgeeks.org/practice-questions-for-recursion-set-6/?ref=lbp