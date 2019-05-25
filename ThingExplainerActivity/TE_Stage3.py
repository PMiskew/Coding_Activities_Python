import tkinter as tk

print("Stage 3")
#VARIABLES: MUST BE CONTAINED IN LIST
a = [1]
list = ["cat","dog","fish","monkey","donkey"]

#FUNCTIONS:
def runMe():
	
	text = textbox.get("1.0",tk.END)

	#When the text is accessed from textbo an enter is placed at the end. 
	#using substring we can access everything except the last character in 
	#the string which is a special character representing the enter
	text = text[:-1]

	#processText removes the last word that was entered
	text = processText(text)
	textbox.delete("0.0",tk.END)
	textbox.insert("0.0",text)
	print(text)


def processText(text):

	newText = text
	for i in range(len(text) - 1, -1, -1):
		if (text[i] == " "):
			word = text[i+1:]

			if word in list:
				print("FOUND")
				newText = text[:i + 1]
				print(newText)
				return newText



	return newText


#WINDOW SETUP:
root = tk.Tk()

textbox = tk.Text(root)
textbox.config(borderwidth = 10)
textbox.pack()

btnProcess = tk.Button(root, text = "Process Text", command = runMe)
btnProcess.pack(fill = tk.BOTH, expand = 1)

root.mainloop()
print("END PROGRAM")