# print positive and negative number

num1=int(input("enter a number"))
if num1>0:
    print("positive")
elif num1==0:
    print("zero")
else:
    print("negative")

print("time complexity","O(1)")
print("space complexity","O(1)")

 # number is odd or even
num1=7

if(num1%2==0):
    print("even")
else:
    print("odd")
print("time complexity","O(1)")
print("space complexity","O(1)")
    
#  Check if a person is eligible to vote (age >= 18).  
age=18
if age >= 18:
    print("you are eligible to vote ")
else:
    print("your not eligible")

print("time complexity","O(1)")
print("space complexity","O(1)")


# greatest of two numbers
num1=10
num2=20.2
if num1>num2:
    print("num 1 is greater") 
elif num1==num2:
    print("equal")
else: 
    print("num2 is greater then mum1") 

print("time complexity","O(1)") 
print("space complexity","O(1)")

# Print "Pass" if a student scores more than 40 marks;  otherwise, print "Fail." 
marks=40
if marks>40:
    print("pass")
else:
    print("fail")

print("time complexity","O(1)")
print("space complexity","O(1)")

   	# Write a program to display the day of the week based on a  number input (1 for Monday, 2 for Tuesday, etc.).  
day=int(input("enter a number for days"))
if(day==1):
    print("sunday")
elif(day==2):
    print("tuesday")
elif(day==3):
    print("wednday")
elif(day==4):
    print("thursday")
elif(day==5):
    print("friday")
elif(day==7):
    print("saturday")
else:
    print("invalid input")

print("time complexity","O(1)")
print("space complexity","O(1)")
    
# Implement a simple calculator to perform addition,  subtraction, multiplication, and division. 












	# Write a program to display the name of a month based on  the month number (1 for January, 2 for February, etc.). 
month=int(input("enter a months"))
if(month==1):
        print("january")
elif(month==2):
        print("feb")
elif(month==3):
        print("march")
elif(month==4):
        print("april")
elif(month==6):
        print("may")
else:
        print("invalid month")

print("time complexity","O(1)")
print("space complexity","O(1)")

# Write a program to find the greatest of three numbers.
num1=float(input("enter a first number:")) 
num2=float(input("enter a second number:"))
num3=float(input("enter a third number:"))

# 	Check if a year is a leap year. 
year=int(input("enter a year"))
if year%2==0:
    print("year is leap year")
else:
    print("not a leap year")
print("time complexity","O(1)")
print("space complexity","O(1)")