# program is to calculating
# any binary no. n

def bin(n):
    if n==0:
        return
    bin(n//2)
    print(n%2,end="")

inp=int(input())
bin(inp)

# Example is from Geeks for Geeks
# https://www.geeksforgeeks.org/practice-questions-for-recursion-set-2/?ref=lbp
