from tkinter import *
from time import strftime

window = Tk()

window.title('clock!')

def time():
    tistr = strftime('%Y , %b , %d, %a  %I : %M : %S %p')
    clock.config(text = tistr)
    clock.after(1000, time)


clock = Label(window, font= ('Times New Roman', 36), bg = 'gold', fg = 'white')
clock.pack(padx = 20, pady = 20)

time() 
window.mainloop() 





