"""
The ecludian way of finding GCD
1
"""


def gcd(a,b):
    if b ==0:
        return a
    
    rem = a%b
    return gcd(b,rem)
    


a=24;b=42

res = gcd(b,a)
print(res)