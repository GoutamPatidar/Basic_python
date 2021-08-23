print("ENTER THE INTERVAL")
a=int(input())
b=int(input())
for num in range(a,b+1):

     if(num>1):
         for x in range(2,num):
             if(num%x==0):
                 break
         else:
                 print(num,end=" ")    