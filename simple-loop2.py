n=int(input())
for i in range(1,n+1):
    if(i==n):
        print("1"*i,end=",")
        print("0"*i,end=" ")
    else:
        print("1"*i,end=",")
        print("0"*i,end=",")