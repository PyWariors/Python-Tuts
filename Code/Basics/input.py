# In Python, input is taken from the user by the input() function

a = input()
print(a)

# You can include a prompt for the input
a = input("Please enter the value of a : ")
print(a)

# All input in Python is taken as a string. To convert the input, we need to typecast it.

a = input("Enter a")
b = input("Enter b")
print(a+b)

# vs

a = (int)(input("Enter a"))
b = (int)(input("Enter b"))
print(a+b)
