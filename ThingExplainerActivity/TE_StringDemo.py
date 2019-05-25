str1 = "Sea Floor"
#prints the string to the screen
print(str1) 
#concatinate strings in the print function using the +
print("The String is"+str1) 
print(str1+" is the String")
print("The String is "+str1+", really!") 

len = len(str1)
print (len)
#use , to concatenate numeric values, note a space is automatically added
print("The length is",len)
#cast to a string and use + to print to concatenate string
print("The length is "+str(len))

print(str1[0])
print(str1[8])
print(str1[6:9])
print(str1[2:])
print(str1[:2])
#negative can be using in Python to go from the end of the string 
#-1 is the last index, -2 is the second last.  I have only seen this
#in Python. 
print(str1[-1])
print(str1[-2:])
print(str1[-3:-1])

#String instance function. Don't memorize these, but understand the 
#input --> process --> Output
#What it takes --> What it does --> What it returns
#I have included a few essential ones. 
loc = str1.index(" ")
print(loc)



