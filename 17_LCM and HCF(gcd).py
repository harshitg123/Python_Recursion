# Python program to calculate the LCM and HCF of two no's

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a, a)

def lcm(a,b):
    return int(a*b/gcd(a,b))
a=5
b=10
# For LCM
print(lcm(a,b))

# For HCF(gcd)
print(gcd(a,b))