list1=[]
for i in range(0,100):
    if i%3==0:
        # list1.append(i)
        list1.extend([i])
print(list1)

# list1=[1,2,3,4,5,6,7,8,]
# print(list1.count(7)) 