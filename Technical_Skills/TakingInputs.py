#Comments are made with a #
#It is essential you comment code. 

#This program will take two integers 
#and multiply them

#Input 
#The input function returns the string the user enter
#All inputs start as Strings
#To change the type of variable you "cast" it
#casting is the process of changing type
name = input("Please input your name: ")
a = input("Please input first number: ")
a = int(a) #self-referencing assignment statment
b = input("Please input second number: ")
b = int(b)

#Process
#What is process 
product = a * b


#Ouput
print("Hi, "+name)
print("The product of "+str(a)+" and "+str(b)+" is "+str(product)+".")

