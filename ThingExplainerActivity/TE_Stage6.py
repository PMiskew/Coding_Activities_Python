import tkinter as tk

print("Stage 6")
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
		
def processText(text):

	newText = text
	loc = 0
	
	word = text[:-1] #assume text is only one word
	wordClean = text[:-1]
	offset = 0

	#look for space starting at end of string.  If a space is found 
	#store last word in word and store the index of the space
	for i in range(len(text) - 2, -1, -1):
		if (text[i] == " "):
			loc = i
			word = text[loc+1:len(text) - 1]
			wordClean = word
			for j in range(0,len(charList),1):
				wordClean = wordClean.replace(charList[i],"")


			offset = len(word) - len(wordClean)
			break;	#break once found


	#if word is not in valid list then process the text string to
	#the new text.  
	if wordClean not in list:
	
		if loc != 0:
			newText = text[:loc + 1]
		else: #This else accounts for teh case of one word text
			newText = ""
			
		return newText



	return newText

def processText1(text):

	offset = 0
	newText = text

	loc = len(text) - 1 #for while loop
	while text[loc] in charList:
		loc = loc - 1
		offset = offset + 1

	print(offset)
	wordClean = text
	locEnd = 0
	for i in range(loc,-1,-1):
		if text[i] == " ":
			locEnd = i
			break;

	if locEnd != 0:
		wordClean = text[locEnd + 1:len(text) - offset]
	else:
		wordClean = text[0:len(text) - offset]

	if wordClean not in list:
		if locEnd != 0:
			newText = text[:locEnd + 1]
		else: #This else accounts for teh case of one word text
			newText = ""
	
	print(wordClean)
	print(newText)
	return newText
	
	
#WINDOW SETUP:
root = tk.Tk()

textbox = tk.Text(root)
textbox.config(borderwidth = 10)
textbox.pack()
textbox.bind("<KeyRelease>",runMe)

root.mainloop()
print("END PROGRAM")