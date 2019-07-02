
import math #Change 1: import math 
#Change 4: Include /n (new line) and /t (tab) escape code for formatting

print("Volume of a Cylinder Formula:\n")
#Input
#What inputs are needed to calculate the volume of a cylinder?
name = input("\n\tWhat is your name: ")		#takes users name

#Change 5: Give some context about the formula
print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03C0\u00d7radius\u00b2\u00d7height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")



radius = input("\n\tInput radius(cm): ")	#input
radius = (int)(radius)					#cast to int

height = input("\n\tInput height(cm): ")	#input
height = (int)(height)					#cast to int
#Process
#What formula is used to calucate the volume of a cylinder?

volume = math.pi*radius*radius*height #Change 1: replace 3.14 with math.pi
volume = round(volume,2)	#Change 2: round the volume to 2 deimal places. 

#Output
#What is important about the output?
#Change 3: Updated output to be more user friendly
print("\n\t\tHi "+name+"!")
print("\n\t\tGive a cylinder with:")
print("\t\tRadius = "+str(radius))
print("\t\tHeight = "+str(height))
print("\t\tThe volume is: "+str(volume)+"\n")	