ar=[]
p=0
dimen1=int(input())
dimen2=int(input())
dimen3=int(input())
n=int(input())
for i in range(dimen1+1):
    for j in range(dimen2+1):
        for k in range(dimen3+1):
            if (i+j+k)==n:
               continue
            else:
               ar.append([])
               ar[p]=[i,j,k]
               p=p+1
print(ar)# Cuboid one in Hackerrank
