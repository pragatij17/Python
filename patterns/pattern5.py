n=int(input())
for i in range(0,n):
    for j in range(1,(2*(n-i)-1)+1):
        if(j<=(n-i)):
            print(j, end=" ")
        else:
            print((n-i)-(j-(n-i)),end=" ")
    print()
