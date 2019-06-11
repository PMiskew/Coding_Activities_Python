import tkinter as tk
from PIL import ImageTk, Image


print("Stage 1 - Photo Editor")
#This creates the main root of an application

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

#Start the GUI
root.mainloop()