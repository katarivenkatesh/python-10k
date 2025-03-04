# fib series
# n=15
# num1=0
# num2=1
# print(num1)
# print(num2)

# for i in range(1,n-1):
#     temp=num1+num2
#     print(temp)
#     num1=num2
#     num2=temp


num1=int(input("enter a number"))
if num1 in [0,1]:
    print("not a prime")
else:
    count=0
    for i in range(1,num1+1):
        if num1%i==0:
            count+=1
    

if count== 2:
     print("prime number")
