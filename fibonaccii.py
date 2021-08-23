a=int(input("ENTER THE NO. YOU WANT TO CHECK "))
n=int(0)
c=int(0)
d=int(1)
while(a>=n):
    e=int(c+d)
    c=d
    d=e
    if(a==e):
        print("GIVEN NO. IS ARMSTRONG NO.")
        break
    n+=1    
if(n>a):
    print("GIVEN NO. IS NOT ARMSTRONG NO.")
