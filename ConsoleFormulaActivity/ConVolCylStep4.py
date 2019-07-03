
import math 


print("Volume of a Cylinder Formula:\n")

print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03C0\u00d7radius\u00b2\u00d7height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")

name = input("\n\tWhat is your name: ")		#takes users name

height = 1
radius = 1

while (radius != 0 or height != 0):
	
	try:
		radius = input("\n\tInput radius(cm): ")	#input
		radius = (int)(radius)						#cast to int

		height = input("\n\tInput height(cm): ")	#input
		height = (int)(height)						#cast to int
	except:
		print("\n\t\tNumeric Type Required")
		height = -1
		radius = -1
	
		volume = math.pi*radius*radius*height 
		volume = round(volume,2)	
	if radius >= 0 and height >= 0:
		print("\n\t\tHi "+name+"!")
		print("\n\t\tGive a cylinder with:")
		print("\t\tRadius = "+str(radius))
		print("\t\tHeight = "+str(height))
		print("\t\tThe volume is: "+str(volume)+"\n")	
	else:
		print("\t\tYou have entered an invalid value.")

print("\t\t\tEND PROGRAM")
