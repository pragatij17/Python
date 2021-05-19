# Random: A, BB, CCC, DDDD, EEEEE, FFFFF….n
n=int(input("Number of element in the series:"))
a=64
for i in range(0,n+1):
    for j in range(0,i):
        print(chr(a),end=" ")
    a+=1