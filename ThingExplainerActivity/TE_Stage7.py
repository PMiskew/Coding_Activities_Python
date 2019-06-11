import tkinter as tk

print("Stage 7")
#VARIABLES: MUST BE CONTAINED IN LIST
badwords = []
list = []
charList = [" ","\n","\r","?","!","."]
#We need /r and /n since when the keystoke is read as an input "Return" resisters as /r
#This gets translated into the string as a new line, which is stored as /n

#FUNCTIONS:
def runMe(event):
	
	if event.char in charList:
		text = textbox.get("1.0",tk.END)

		#When the text is accessed from textbox an enter is placed at the end. 
		#using substring we can access everything except the last character in 
		#the string which is a special character representing the enter
		text = text[:-1]

		#processText removes the last word that was entered
		text = processText1(text)
		textbox.delete("0.0",tk.END)
		textbox.insert("0.0",text)
		
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
		if text[i] == " " or text[i] == "\n":
			locEnd = i
			break;

	if locEnd != 0:
		wordClean = text[locEnd + 1:len(text) - offset]
	else:
		wordClean = text[0:len(text) - offset]

	if wordClean not in list:
		badwords.append(wordClean)
		if locEnd != 0:
			newText = text[:locEnd + 1]
		else: #This else accounts for teh case of one word text
			newText = ""

	print(badwords)
	return newText
	
	
#WINDOW SETUP:
root = tk.Tk()

textbox = tk.Text(root)
textbox.config(borderwidth = 10)
textbox.pack()
textbox.bind("<KeyRelease>",runMe)

#Load List
wordFile = open("wordlist.txt",'r')
for line in wordFile:
	list.append(wordFile.readline()[:-1])

print(list)




root.mainloop()
print("END PROGRAM")