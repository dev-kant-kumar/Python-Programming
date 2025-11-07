# Python support all types of numbers with high precision

# Integer
a = 10
b = 9
c= 3.2
d = 2 + 5j

print("Value of (a , b , c , d ) : ",( a,b,c,d) )
print("a + b : " , a + b)
print("a - b : " , a - b)
print("a * b : " , a * b)
print("a / b : " , a / b)
print("a // b : ", a // b)
print( "a == b : ",a == b)
print("a != b : " ,a != b)
print( "a > b : " , a > b)
print("a < b < c : ",a < b < c )
print("( a < b) and (b < c) : ",( a < b) and (b < c)) # more readable and prefer syntax
print("(a > b ) or not(b > c) : ",(a > b ) or not(b > c))
print("Left shift : " , a << 2)
print("Right shift : " , a >> 2)

result = 0.3 + 0.3 + 0.3
print("result : " ,result)
print("result - 0.9 : " , result - 0.9)
# not getting expected result in above case

# to fix this issue we have decimal module
from decimal import Decimal
fixedRes =  Decimal("0.3") + Decimal("0.3") + Decimal("0.3")
print("fixedRes : ", fixedRes)
print("result - 0.9 : " , fixedRes - Decimal("0.9"))


print("(2 + 5j) + 15 : ", (2 + 5j) + 15)
print("(2 + 5j) + 15j : ", (2 + 5j) + 15j)
print("(2 + 5j) - (10 + 9j) : ", (2 + 5j) - (10 + 9j))
print("(2 + 5j) * (10 + 9j) : ", (2 + 5j) * (10 + 9j))
print("(2 + 5j) * 5 : ", (2 + 5j) * 5)

print("Power", 2 ** 100)
print("Power with float : " , 100 ** 2.3)

# numbers with different base : binary(2) , octal(8) , hexadecimal(16)

print("binary of 987 : ", bin(987))
print("binary of 0b10101 : ", int("0b10101",2))
print("0b10101 : " , 0b10101)

print("Octal of 987 : ", oct(987))
print("Octal of 0o1234567 : ", int("0o1234567",8))
print("0o1234567 : ", 0o1234567)

print("Hexadecimal of 987 : ", hex(987))
print("Hexadecimal of 0x123e4f5 : ", int("0x123e4f5",16))
print("0x123e4f5 : ", 0x123e4f5)

import math

print("math.ceil(3.13) : ", math.ceil(3.13))
print("math.floor(3.13) : ", math.floor(3.13))
print("math.ceil(-3.13) : ", math.ceil(-3.13))
print("math.floor(-3.13) : ", math.floor(-3.13))
print("math.trunc(3.1) : ",math.trunc(3.1))
print("math.trunc(-2) : ",math.trunc(-2.9))


import random

randomNum = random.random()
opt = int(randomNum * 1000000 )

print("opt : " ,opt)
print("randomNum : " ,randomNum)

print("Randomly selected no from 1 to 9  :" ,random.choice([1,2,3,4,5,6,7,8,9]))
print("Random no from range 1 to 10 " ,random.randrange(1,10))

topics = ["Networking","Operating System" , "Database","System Design"]
random.shuffle(topics)
print("Shuffled topics : " , topics)

