
a=int(input("enter any no."))
def fact(a):
  if(a<=1):
    return 1
  return(a*fact(a-1))
print(fact(a))
 