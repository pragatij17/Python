n=int(input("Enter the last digit:"))
for i in range(1,n+1):
    if(i==n):
        print(i,end="")
    else:
        print(i,end=",")