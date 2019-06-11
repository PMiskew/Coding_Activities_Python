import tkinter as tk

print("Stage 5")
#VARIABLES: MUST BE CONTAINED IN LIST
a = [1]
list = ["cat","dog","fish","monkey","donkey"]
charList = [" ","\r","?","!","."]
#FUNCTIONS:
def runMe(event):
	
	if event.char in charList:
		text = textbox.get("1.0",tk.END)

		#When the text is accessed from textbo an enter is placed at the end. 
		#using substring we can access everything except the last character in 
		#the string which is a special character representing the enter
		text = text[:-1]

		#processText removes the last word that was entered
		text = processText1(text)
		textbox.delete("0.0",tk.END)
		textbox.insert("0.0",text)
		print(text)

def processText1(text):

	newText = text #This is the text to send back that will update the display - Defaults to text
	wordClean = text #This stores the last word in the sentence to inspect - defaults to text
	
	#This loop finds the space before the last word.  This will allow us to pull out
	#last word store it in wordClean and then process it to see if it is valid.
	#If the loop gets all the way to 0 then there is only one word on the display
	locEnd = 0
	for i in range(len(text) - 2,-1,-1):
		if text[i] == " ":
			locEnd = i
			break;
	
	#This pulls out the last word and stores in wordClean
	if locEnd != 0:
		wordClean = text[locEnd + 1:len(text) - 1]
	else:
		wordClean = text[0:len(text) - 1]

	#Checks to see if wordClean is a valid word.  If it is not then
	#the program removes it and stores the result in newText
	if wordClean not in list:
		if locEnd != 0:
			newText = text[:locEnd + 1]
		else: #This else accounts for teh case of one word text
			newText = ""
	print(newText)
	#This sends back the text to be processed	
	return newText
	
def processText(text):

	newText = text
	loc = 0
	
	word = text[:-1] #assume text is only one word



	#look for space starting at end of string.  If a space is found 
	#store last word in word and store the index of the space
	for i in range(len(text) - 2, -1, -1):
		if (text[i] == " "):
			loc = i
			word = text[loc+1:len(text) - 1]	
	
			break;	#break once found


	#if word is not in valid list then process the text string to
	#the new text.  
	if word not in list:
	
		if loc != 0:
			newText = text[:loc + 1]
		else: #This else accounts for teh case of one word text
			newText = ""
			
		return newText



	return newText


#WINDOW SETUP:
root = tk.Tk()

textbox = tk.Text(root)
textbox.config(borderwidth = 10)
textbox.pack()
textbox.bind("<KeyRelease>",runMe)

root.mainloop()
print("END PROGRAM")