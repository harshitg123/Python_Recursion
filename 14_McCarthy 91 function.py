# The program ha it's standard name i.e
# McCarthy 91 function
# you will get more info on wikipedea
# https://en.wikipedia.org/wiki/McCarthy_91_function

def fun(n):
    if n>100:
        return n-10
    else:
        return fun(fun(n+11))
print(fun(int(input())))

# Explanation of the above code:
'''
fun(99) = fun(fun(110)) since 99 < 100        if cond -> False
           = fun(100)    since 110 > 100      if cond -> True
           = fun(fun(111)) since 100 = 100    if cond -> False
           = fun(101)    since 111 > 100      if cond -> True
           = 91        since 101 > 100        if cond -> True -> return 91
'''
# visit to Geeks for Geeks for more info.
# https://www.geeksforgeeks.org/practice-questions-for-recursion-set-5/?ref=lbp
