# Program for checking that 
# a gin=ve number or a string is palindrome or not
# This Program can check both string and no.

def ispalindrome(n):
    if len(n)<=0:
        return ("True")
    else:
        if n[0] == n[-1]:
            return ispalindrome(n[1:-1])
        else:
            return "False"
print(ispalindrome(input()))            
            