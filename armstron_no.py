a=int(input("ENTER ANY NO."))
b=a 
n=0
c=0
d=0
while(b!=0.0):
    b=int(b/10)
    n+=1
    print(a,"  ",b,"  ",n)
print(a,"  ",b)
b=a
print(a,"  ",b,"  ",n)
while(b!=0):
    c=b%10
    d=d+round(pow(c,n))
    b=int(b/10)
if(a==d):
    print("armstrong no.")
else:
    print("not a armstrong no.")
