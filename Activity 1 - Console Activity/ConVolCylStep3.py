import math


print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03C0 \u00D7 radius\u00B2 \u00D7 height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")

#Input
#What inputs are needed to calculate the volume of a cylinder?
name = input("\n\tWhat is your name: ")

radius = 1
height = 1

while (radius != 0 or height != 0):

	radius = input("\n\tInput radius (cm): ")
	radius = int(radius)

	height = input("\n\tInput height (cm): ")
	height = int(height)
	#Process
	#What formula is used to calculate the volume of a cylinder?
	#V = pi * r * r * h
	
	if (radius >= 0 and height >= 0):

		volume = math.pi * radius * radius * height
		volume = round(volume,2)
		#Output
		#What is important about the output?
		print("\n\t\tHi "+name+"!")
		print("\n\t\tGive a cylinder with:")
		print("\t\tRadius = "+str(radius))
		print("\t\tHeight = "+str(height))
		print("\t\tThe volume is: "+str(volume)+"\n")	
	else: 
		print("\n\t\tYou have entered an invalid value")
	#Checks while boolean expression

print("END PROGRAM")

'''
Block Comments are started using three single quotes

User Requirements:
	- The program should only prompt for the user name once. 
    - The program should report an error if one or both values 
      entered are negative. 
    - The program should exit if the user enters 0 for both height 
      and radius. 

1) Constructing a while loop
	
	while (boolean expression):
		<while code block>
		<while code block>
		<while code block>

2) Initialization of variables
3) Simple if else strucutre
	
	if (boolean expression):
    	<if code block>
    	<if code block>
    	<if code block>
	else:
    	<else code block>
    	<else code block>
    	<else code block>
4) Boolean operators


Block Comments are ended using three single quotes

'''










