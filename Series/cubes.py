# Cubes: 1,8,27,64...n
n=int(input("Last element of the series:"))
for i in range(1,n+1):
	print(i*i*i,end=",")