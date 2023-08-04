x = 4 # x is of type int 
#x = "Sally" # x is now of type str
print("The value of x is: ", x)
print("The type of x before: " , type(x))

#casting a datatype to a variable
y = str(x)
print("The type of x after: " , type(y))

#Case sensitivity in assigning variables in python
a = 4
A = "Sally" #A will not overwrite a 
print(A)
print(a)

#Assigning multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Printing multiple variables using comma operator
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#printing multiple variables using + operator
x = "Python is "
z = "awesome in 2023"
print(x + z)

#Creating a function and testing global variables
b = "the most popular language in 2023."
def myfunc():
    global b 
    b = "fantastic"
    print("Python is " + b)

myfunc()
print("Python is " + b) 





