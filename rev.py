#print natural number

num=int(input("enter a number"))
sum=0
for i in  range (1,num+1):
    sum=i+sum
print(sum)

#approach2
print((num*(num+1))/2)