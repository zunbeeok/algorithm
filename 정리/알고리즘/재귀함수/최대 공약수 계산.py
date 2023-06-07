def gcd(a, b):
    re = a % b
    print(re)
    if(re == 0 ):
        return b
    return gcd(b, re)


print("두수의 최대 공약수는? ", gcd(192, 162))