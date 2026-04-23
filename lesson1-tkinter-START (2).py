'''
Project Name:Screen Pet
Author:Jaksh
Date:2025-09-04

This is a title block! Title blocks help you keep track of the purpose and 
progress of a project. We will be including one at the beginning of all projects
from now on.

After filling out the 3 pieces of information, write a short blurb on 
what this project does and how to use it! This only needs to be two sentences
for this simple project.
'''


'''
TODO:
- create a canvas with a
    - background colour
    - size

- using lines, polygons, rectangles, and ovals, draw an animal on your canvas
- tag all your canvas objects!
'''





def print_loc(event):
    '''
    This function is made for you to help you get familiar with the grid on the
    screen!

    It will print out the X, Y coordinates of any point you want.
    When your program is running, simply click (using left moust button)
    on the point on the canvas you want the location of.
    The output will be in the shell!

    '''
    print(event.x, event.y)

from tkinter import *
# Your window has been made for you below
root = Tk()

# this line allows our print function to be called when and wherever you click
root.bind("<Button-1>", print_loc)
c =  Canvas(root, height=600, width=600, bg='yellow')
c.create_rectangle(50, 50, 550, 550, fill="light blue",
tags=('frame'))
c.create_oval(200, 200, 400, 400, fill="light green", tags=('head'))
c.create_line(300, 350, 325, 370,fill="dark green", tags=('mouth'))
c.create_line(300, 350, 275, 367,fill="dark green", tags=('mouth'))
c.create_oval(256,265, 296,304, fill="white", tags=('eye1'))
c.create_oval(269,278,284,293, fill="black", tags=('eye1irus'))
c.create_oval(308,268,339,301, fill="white", tags=('eye2'))
c.create_oval(321,280,332,292, fill="black", tags=('eye2irus'))
c.create_rectangle(352,200,240,147,fill="blue",tags=('hat'))
c.create_rectangle(353,187,399,201,fill="white",tags=('hat'))
c.pack()
# Create your canvas and all your canvas objects here! Don't forget to pack!

# Do not remove this line! It keeps your window open while the code is running
root.mainloop()
