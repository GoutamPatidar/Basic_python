matrix=[]
r=int(input("no. of row"))
c=int(input("no. of colom"))
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
matrix1=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix1.append(a) 
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(r):
    for j in range(c):
        result[i][j]=matrix[i][j]+matrix1[i][j]
for i in range (r):
    for j in range(c):
        print(result[i][j],end=" ")
    print()
      