# For a positive n, fun2(n) prints the values of 
# n, 2n, 4n, 8n … while the value is smaller than LIMIT. 
# After printing values in increasing order, it prints 
# same numbers again in reverse order.

def fun2(n):
    Limit=1000
    if n<=0:
        return(print("Not entred correct value!"))
    if n>Limit:
        return
    print(n)
    fun2(n*2)
    print(n)
fun2(int(input()))

# For better understanding plz visit on to the geeks for geeks
# https://www.geeksforgeeks.org/practice-questions-for-recursion-set-3/?ref=lbp