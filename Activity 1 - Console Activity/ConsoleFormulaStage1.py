#In this stage we will make a simple program that takes in 
#values from the user and outputs the resulting calculation
#Some chnage


print("Volume of a Cylinder Formula: ")
name = input("Please input your name: ")
print("The volume of a cylinder is")
print("V = (1/3)*pi*r\u00b2")

#Input
radius = input("Input radius(cm): ")
radius = (int)(radius)

height = input("Input height(cm): ")
height = (int)(height)

#Process
volume = 3.14*radius*radius*height

#Output
print("The volume of a cylinder with,")
print("radius = "+str(radius)+" cm")
print("height = "+str(height)+" cm")
print("is V = "+str(volume)+ " cm\u00b3")