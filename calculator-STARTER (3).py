'''
Calculator Builder - Starter Code
Author:Jaksh
Date:2026-03-19
'''


from tkinter import *
root = Tk()
expression = StringVar()
root.geometry('200x250')
expression = StringVar()

class CalcButton():
    def __init__(self,frame,char,bgcol,fgcol,row,col,command=None): 

        
        self.char = char
        
        if command == None:
            command = self.onClick

        self.obj = Button(frame, bg = bgcol, fg = fgcol, text = char, command=command, padx=16, pady=20)
        self.obj.grid(row=row, column=col, sticky='news')
  

    def onClick(self):
        
        expression.set(expression.get() + self.char)


def clear():
 

    expression.set('')


def delete():
    

    
    expression.set(expression.get()[:-1])


def evaluate():
    
    try:
        result = str(eval(expression.get()))
        expression.set(result)
    except Exception:
        expression.set('Error')

f1 = Frame(root, bg = 'light grey', padx= 26, pady= 50)
f1.grid(row = 0, column = 0, columnspan= 6,rowspan= 6, sticky = 'news')

textbox = Label(f1, bg='white', textvariable=expression, justify='right', relief='sunken', width=f1.winfo_width(), padx= 16, pady= 13)
textbox.grid(row= 3, column=0 , columnspan= 5, sticky= 'news')

num_frame = Frame(f1,bg='light grey',padx=20,pady=15)
num_frame.grid(row=5, column=0, columnspan= 4, sticky='news')

other_buttons_frame = Frame(f1,bg='light grey',padx=20,pady=15)
other_buttons_frame.grid(row=4, column=0, columnspan= 1, sticky='news')

CalcButton(other_buttons_frame, 'CLR', 'grey','black',0,0,command=clear)
CalcButton(other_buttons_frame, 'DEL', 'grey','black',0,1,command=delete)
CalcButton(other_buttons_frame, 'OFF', 'grey','black',0,2,command=root.quit)

CalcButton(num_frame, '7', 'orange', 'black', 0,0)
CalcButton(num_frame, '8', 'orange', 'black', 0,1)
CalcButton(num_frame, '9', 'orange', 'black', 0,2)
CalcButton(num_frame, '4', 'orange', 'black', 1,0)
CalcButton(num_frame, '5', 'orange', 'black', 1,1)
CalcButton(num_frame, '6', 'orange', 'black', 1,2)
CalcButton(num_frame, '1', 'orange', 'black', 2,0)
CalcButton(num_frame, '2', 'orange', 'black', 2,1)
CalcButton(num_frame, '3', 'orange', 'black', 2,2)
CalcButton(num_frame, '0', 'orange', 'black', 3,0)

CalcButton(num_frame, '/', 'brown2', 'black', 0,3)
CalcButton(num_frame, '*', 'brown2', 'black', 1,3)
CalcButton(num_frame, '+', 'brown2', 'black', 2,3)
CalcButton(num_frame, '-', 'brown2', 'black', 3,3)
CalcButton(num_frame, '.', 'brown2', 'black', 3,1)
CalcButton(num_frame, '=', 'brown2', 'black', 3,2,command=evaluate)

root.mainloop()