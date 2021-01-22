n=int(input())
cnt=0
h=0
while(cnt<=n):
    h+=1
    cnt+=(h*(h+1)/2)
print(h-1)
