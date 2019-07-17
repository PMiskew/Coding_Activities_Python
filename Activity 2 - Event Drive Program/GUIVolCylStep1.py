import tkinter as tk
import math


#VARIABLES
root = tk.Tk()
file = open("data.txt","w")

#FUNCTIONS

def runMe(*args):
	print("running")
	
	#Access Text
	r = entRadius.get()
	h = entHeight.get()


	try: 
		r = float(r)
		h = float(h)


		if (r >= 0 and h >= 0):
			v = calcVolume(r,h)
			print(v)
			display.config(state ="normal")
			strDisplay = "Volume of Cylinder:\nradius = "+str(r)+"\nheight = "+str(h)+"\nvolume = "+str(v)
			display.delete(1.0,tk.END)
			display.insert(tk.END,strDisplay)
			file.write(str(v)+"\n")
		else:
			print("BAD INPUT")
	except:
		print("ERROR - STRING INPUT NEED NUMBER")

	entRadius.delete(0,tk.END)
	entHeight.delete(0,tk.END)

def calcVolume(radius, height):


	volume = math.pi*radius*radius*height 
	volume = round(volume,2)	
	return volume








label = tk.Label(root,text = "Volume Calculator")
label.pack()

labRadius = tk.Label(root,text = "Radius (cm)")
labRadius.pack()

entRadius = tk.Entry(root)
entRadius.pack()

labHeight = tk.Label(root, text = "Height (cm)")
labHeight.pack()
entHeight = tk.Entry(root)
entHeight.pack()

btn = tk.Button(root, text = "Calculate Volume", command = runMe)
btn.pack();

display = tk.Text(root,height = 5, width = 20)
display.config(state = "disabled")
display.pack()

root.bind("<Return>",runMe)


#MAIN LOOP
root.mainloop()
file.close()

