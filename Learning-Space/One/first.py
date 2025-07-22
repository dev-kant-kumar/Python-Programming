print("Welcome to python programming")

# firstName = input("Enter first name : ")
# middleName = input("Enter middle name : ")
# lastName = input("Enter last name : ")
# age = int(input("Enter age : "))
# isMinor = False


# print("Here is your info")
# print(f"Your fullname is : {firstName + middleName + lastName}")

# if(age>=18) :
#     print("You are major")
# else :
#     print("You are minor")    

# function section

def add(num1,num2):
    return num1+num2

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

print(f"Sum of {num1} and {num2} : {add(num1,num2)}")
