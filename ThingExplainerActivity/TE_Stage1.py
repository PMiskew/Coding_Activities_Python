import tkinter as tk

print("Stage 1 - TE")

#VARIABLES: MUST BE CONTAINED IN LIST
a = [1]

#FUNCTIONS:
def runMe():
	print("Running")
	
	a[0] = a[0] + 1
	print(a[0])xx

#WINDOW SETUP:
root = tk.Tk()

textbox = tk.Text(root)
textbox.config(borderwidth = 10)
textbox.pack()

btnProcess = tk.Button(root, text = "Process Word", command = runMe)
btnProcess.pack(fill = tk.BOTH, expand = 1)

root.mainloop()
print("END PROGRAM")