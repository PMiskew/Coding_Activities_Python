#Assignment Statements:
#	An assignment statement is a line of code with an = 
# 	<Variable Name> = <Information to be Stored>
#	Always evaluate right side first and store in variable
#	location. 

#Self-Referencing Assignment Statement
#	A self-referencing assignment statement is an assignment
#	statement that accesses the variable where the value will
#	be stored. 

x = 4 #Declared 
print(x)
x = 6 + 9
print(x)
x = x + 1 # x = 15 + 1 
print(x)

name = "Bob"
print(name)
name = name + " Smith"
print(name)
name = "Bob Smith"
print(name)

y = 3 + 8.0 #3 + 8.0 = 11.0
print(y)
y = y * 3 #11.0 * 3 = 33.0
print(y)
y = y /2 # 33.0/2 = 16.5
print(y)









