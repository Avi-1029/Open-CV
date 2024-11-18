from tkinter import *
import tkinter.font as fn
from random import *

window = Tk()

window.geometry('900x500')

fnt = fn.Font(family = 'Times New Roman', size = 14 )

window.config(bg = 'pale violet red')

window.title('Rock, Paper, Scissors!')

compchoice = ['Rock', 'Paper', 'Scissors']
pn = 0
cn = 0

def ground(playerchoice):
    global pn, cn
    chs = choice(compchoice)
    compsel.configure(text = 'Computer Selected: ' + chs)
    playsel.configure(text = 'Player Selected: '+ playerchoice)
    if chs == playerchoice:
        r = 'Tie'
    elif (playerchoice =='Rock' and chs == 'Scissors') or (playerchoice =='Paper' and chs == 'Rock') or (playerchoice =='Scissors' and chs == 'Paper'):
        r = 'Player Wins! AHHAHAHAHAH.'
        pn = pn + 1
    else:
        r = 'COMPUTER WINS AHAHHA LOSER'
        cn = cn + 1
    result.configure(text = r, fg= 'maroon')
    compscore.configure(text = 'Computer Score: '+ str(cn))
    playscore.configure(text = 'Player Score: '+ str(pn))

heading = Label(window, text = "ROCK, PAPER, SCISSORS!", font =('Times New Roman', 25, 'bold'), fg= 'maroon', bg = 'pale violet red' )
heading.grid(row = 0, column = 0, columnspan = 4, padx = 250)

result = Label(window, bg = 'pale violet red')
result.grid(row = 1, column = 0, columnspan = 4, padx = 250)

option = Label(window, text = 'Your Option: ', font = fnt, fg= 'maroon', bg = 'pale violet red' )
option.grid(row = 2, column = 0, padx = 130)

rock = Button(window, bg = 'PaleVioletRed1', fg = 'PaleVioletRed4', text = 'Rock', font = fnt, command = lambda: ground(compchoice[0]))
rock.grid(row = 2, column = 1)

paper = Button(window, bg = 'PaleVioletRed1', fg = 'PaleVioletRed4', text = 'Paper', font = fnt, command = lambda: ground(compchoice[1]))
paper.grid(row = 2, column = 2)

scissors = Button(window, bg = 'PaleVioletRed1', fg = 'PaleVioletRed4', text = 'Scissors', font = fnt, command = lambda: ground(compchoice[2]))
scissors.grid(row = 2, column = 3)

score = Label(window, text = 'Score: ', font = fnt, fg= 'maroon', bg = 'pale violet red' )
score.grid(row = 3, column = 0, padx = 130, pady = 20)

compsel = Label(window, text = 'Computer Selected: ',   bg = 'pale violet red', fg = 'PaleVioletRed4', font = fnt)
compsel.grid(row = 3, column = 1)
playsel = Label(window, text = 'Player Selected:' ,  bg = 'pale violet red', fg = 'PaleVioletRed4', font = fnt)
playsel.grid(row = 4, column = 1)
compscore = Label(window, text = 'Computer Score: ' ,  bg = 'pale violet red', fg = 'PaleVioletRed4', font = fnt)
compscore.grid(row = 3, column = 3)
playscore = Label(window, text = 'Player Score: ' ,  bg = 'pale violet red', fg = 'PaleVioletRed4', font = fnt)
playscore.grid(row = 4, column = 3)


window.mainloop()