from tkinter import *

window = Tk()
window.geometry('900x500')

#Window Title
window.title('Log in NOW!')

#Background colour
window.config(background='lightpink')

u = Label(window, text = 'Username :', bg = 'lightpink')
p = Label(window, text = 'Password :', bg = 'lightpink')

#Another way to add widgets on your window
u.place(x = 60, y = 100)

p.place(x = 60, y = 120)

#Creating entry boxes 
pe = Entry(window, show = '*')
ue = Entry(window)

ue.place(x = 125, y = 100)
pe.place(x = 125, y = 120)

Login = Button(window, text = 'Log in')
Cancel = Button(window, text = 'Cancel')

Login.place(x = 70 , y = 145)
Cancel.place(x = 125, y = 145)

window.mainloop()