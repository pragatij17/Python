list1=[1,2,3,4,5,6,7,1,1,1,4,5,5,6,7]
dict1={}
for element in list1:
    if element in dict1:
        dict1[element]+=1
    else:
        dict1[element]=1
print(dict1)