
name = input("Enter your name : ")
age= int(input("Enter age : "))
marks = int(input("Enter your marks : "))

#check if the user is able to vote or not
print("\nResult for vote :")
if(age>=18):
    print("You are eligible to vote")
else:
    print("You are not eligible tov vote")   

#provide grade based on marks 
print("\nResult for marks :")
if(marks>90 and marks<=100):
    print("Grade A")
elif(marks>80 and marks <=90):
    print("Grade B")
elif(marks>70 and marks <=80):
    print("Grade C")
elif(marks>60 and marks <=70):
    print("Grade D")
else:
    print("Grade E")  


print("\nThis is the end of the code")    