# mutable vs immutable : It's related to memory not value stored .

# Immutable : The object content at memory location can't be changed
# any modification creates a new object
# Integer , Float , Boolean , String , None , Tuple

# example :

# Number : Integer and Float

age = 20
# it allocates the memory for 20 and assign its reference to age .
# and age doesn't have data types info instead its only associated with 20 (the value itself).
print("Age : " + str(age))


age = 22
# here in this case
# new memory is allocated to store 22 and age now refer that memory .
# so we can see that we can't change number , instead its reference changes .
# and old ref will be freed by garbage collector but for number ,
# python will keep that for sometimes to optimise the memory for its future usage.

print("Age : " + str(age))


a = 5
b = a + 5

# here in case of 'b' (5 + 5)
# first the reference of 'a' is calculated and then 5 is added
# a new reference will be created to store the result : 10


print("Value of a : " + str(a))
print("Value of b : " + str(b))


# string

name = "Dev Kant Kumar"
print("Name : " + name)

# name[0] = "d"
# here we are trying to change string , but we can't do this . string is immutable

print("Name : " + name.lower())
#here it will create a new reference


# Mutable : The object content at same memory location can be changed
# list , dictionary


# Example of mutable

list1 = [1,2,3]
print(list1)

list2 = list1
print(list2)


list1[0] = 77 # list is mutable so we can change the value
print(list1)
print(list2)

# here list1 and list2 both refer to same memory
# so changes in one reflect into other too.
# to confirm

print("Is list1 == list2")
print(list1 == list2) # check the equality for values

print("Is list1 is List2")
print(list1 is list2) # check the equality for memory reference


list2 = [1,2,3] # here we create a new reference , so changes into this only not reflect to list1
list2[0] = 55
print("list1")
print(list1)

print("list2")
print(list2)

print("Is list1 == list2")
print(list1 == list2) # check the equality for values

print("Is list1 is List2")
print(list1 is list2) # check the equality for memory reference

print("Memory address of list1")
print(id(list1))
print("Memory address of list2")
print(id(list2))


