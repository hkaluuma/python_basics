#declaring our string and int variables
sName = "Mr. Kaluuma"
iAge = 40
print("Your name is: " + sName)

#The statement below would produce an error.
#print("The age is: "+ iAge)#this failed because of the datatype of str (text) with integer
print("The age is: ", iAge)

#We shall need to do type casting.
#print("The age is: "+ str(iAge))

#print("Hey " + str(7))

#lets check if white space is printed
a = "Hello, World!"
print(a[7])

#looping through a string
for x in "banana":
  print(x)

#length of a string
a = "Hello, World!"
print("String length is: ", len(a))

#Slicing a string
b = "Hello,c World!"
print("The sliced string is: ", b[2:5])

#slicing from the start
b = "Hello, World!"
print("Sliced from the start: ", b[:5])




