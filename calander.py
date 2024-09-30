from tkinter import *
import calendar

def sc():
   window2 = Tk()
   #window2.geometry('400x400')
   
   window2.title('Calander')
   
   window2.config(background= 'plum2')

   y = int(year.get())
   cal = calendar.calendar(y)

   calt = Text(window2, height = 400)
   calt.insert(END, cal)
   calt.pack(padx = 20, pady = 20)

   window2.mainloop()
 

window = Tk()
window.geometry('350x250')

window.title('Calander')

window.config(background= 'plum2')

c = Label(window, text = 'CALANDER', bg = 'plum4', fg = 'plum2', font = ('Comfortaa', 25, 'bold') )
c.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 3)

e = Label(window, text = 'Enter Year: ', fg = 'plum4', font = ('Comfortaa', 10))
e. grid (row = 1, column = 0, padx = 30, pady = 10)

year = Entry(window)
year.grid(row = 1, column = 2, padx = 30, pady = 10)

show = Button(window, text = 'Show Calander', fg = 'plum4', command = sc)
exit = Button(window, text = 'Exit', fg = 'plum4', command = exit)

show.grid(row = 2, column = 0, padx = 10, pady = 10, columnspan = 3)
exit.grid(row = 3, column = 0, padx = 10, pady = 10, columnspan = 3)


window.mainloop()
