import tkinter as tk
from PIL import ImageTk, Image


print("Stage 2 - Photo Editor")
#This creates the main window of an application


def runMe(): 
	print("Running")


root = tk.Tk()
root.title("Join")
root.geometry("600x780")
root.configure(background='grey')

path = "images/100_Fermium.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")



from PIL import Image

im = Image.open('dead_parrot.jpg') # Can be many different formats.
pix = im.load()
print im.size  # Get the width and hight of the image for iterating over
print pix[x,y]  # Get the RGBA Value of the a pixel of an image
pix[x,y] = value  # Set the RGBA Value of the image (tuple)
im.save('alive_parrot.png')  # Save the modified pixels as .png


#Start the GUI
root.mainloop()