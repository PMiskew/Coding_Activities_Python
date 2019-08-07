print("This is an example of variables in Python")

#Concept (Simplified):
#	Think of a variable like a box with a name where something is stored.
#	Programming languages need to know what is inside the box so it knows
#	how big the box needs to be. The type of data stored in a vairable is 
#	refered to as "type".
#
#Declaration:
#	The first time a variable is encountered it is delcared.
#	Declaring a variable allocates memory based on type. 

#Initialization: 
#	This is the value that is placed inside a variable the
#	first time it is used. 

#Assignment statement:
#	An assignment statement is a line of code with an = 
# 	<Variable Name> = <Information to be Stored>
#	Always evaluate right side first and store in variable
#	location. 

#Broad Variable Classifications: 
#	Primitive Type: Stores information at the location in memory
#	Reference Type: Stores a memory reference to where data is in 
#					memory.

#Strings - Acts like Primitive Type
name = "Paul" #String Variable
sentence = "This is a string variable!"
number1 = "3"
number2 = "3.0"

#Integers 32 bits - Primitive Type
num1 = 3
num2 = -9
num3 = 3 + 4

#Floats 32 bits - Primitive Type
fnum1 = 3.0
fnum2 = -9.345
fnum3 = 3 + 4.0 #Store 7.0

#Boolean - Acts like Primitive Type
flag1 = True
flag2 = False

#Lists - Reference Type
#lists have length and index values.  Index values for a list are
#from 0 to length - 1.  
list1 = []
list2 = [1,2,3]
list3 = ["cat","dog"]
list4 = [1,"cat"]
print("The value of element 1 located at index 0 for list 2 is: ",list2[0])
print("The lenght of list 2 is ",len(list2))


