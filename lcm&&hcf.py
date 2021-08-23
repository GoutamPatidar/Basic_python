def gcd(n,m):
    if(n<0 or m<0):
        return -1
    elif(n==0):
        return m
    elif (m==0):
        return n
    else:
        return gcd(m,m%n)
n=int(input())
m=int(input())
lcm=n*m/gcd(n,m)
print(lcm)