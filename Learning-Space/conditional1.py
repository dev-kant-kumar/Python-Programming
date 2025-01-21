# Programs on conditional statements
import os
os.system("cls")


#wap to check entered number is even or odd
num = int(input("Enter a num : "));

if(num%2==0):
    print(num, "is even number")
else:
    print(num, "is odd number")    

# wap to find the greatest of 3 numbers entered by the user
num1= int(input("Enter first num : "))
num2= int(input("Enter second num : "))
num3= int(input("Enter third num : "))

if(num1>num2 and num1>num3):
    print(num1," is greatest")
elif(num2>num1 and num2>num3):
    print(num2, " is greatest")
else:
    print(num3, " is greatest")       

# wap to check if a number is a multiple of 7 or not 
print("_"*150);
number = int(input("Enter the number : "))
if(number%7==0):
    print("This is multiple of 7") 
else:
    print("This is not the multiple of 7")       


