from tkinter import *

#Creating the main window

window = Tk()

#Setting Dimentions to the Window

window.geometry('900x500')

#Putting a button

sikebutton = Button(window, text = 'Hit me for a prize', command = window.destroy)

#Adding the button to the window

sikebutton.pack(side = 'bottom')

#Displaying window ( Always at the end of the code)

window.mainloop()