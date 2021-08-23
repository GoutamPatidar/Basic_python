print("position nth multiple of kth no..")
def position(n,k):
      a=0
      b=1
      i=2
      while(i!=0):
          c=a+b
          a=b
          b=c
          if(b%k==0):
              return n*i 
          i+=1
n=int(input("ENTER THE MULTIPLE NO."))
k=int(input("ENTER WHOSE MULTIPLE SHOULD FIND "))
print("position of nth multiple of k is ",position(n,k))

        