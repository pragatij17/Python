first_num=1
second_num=2
n=int(input("N:"))
for j in range(0,n):
    if(j==0):
        print(first_num,end=",")
    elif j==1:
        print(second_num,end=",")
    else:
        print((first_num*second_num),end = ",")
        temp=first_num
        first_num = second_num
        second_num = temp*second_num