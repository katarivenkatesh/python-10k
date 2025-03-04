# Check if a given number is a prime number using a for loop. 


a=int(input("enter a number"))
flag=True
if a<=1:
    print("not a prime number")
for i in range(2,a):
    if a%i==0:
        print("not a prime")
        flag=False
if flag:
    print("it is a prime")

# Write a program to calculate the factorial of a number using a while loop.

a=int(input("enter anumber"))
fact=1
while a>0:
    fact*=a
    a-=1
print(fact)

#  iv. Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop. -->
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
