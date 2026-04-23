from tkinter import *
root = Tk()
# title = Label(root,padx=100, pady=100, bg = 'black', fg = 'white', text = 'Title')
# title.pack(fill = Y)

# b1 = Button(root, bg = 'red', fg = 'white', text = 'Left Button',width = 20)
# b2 = Button(root, bg = 'green', fg = 'white',text = 'Very Very Long Text Button', width = 20)
# b3 = Button(root, bg = 'blue', fg = 'white',text = 'Right Button',width = 20)

# b1.pack(side = RIGHT)
# b2.pack(side = LEFT)
# b3.pack(side = RIGHT)
# root.mainloop()

title = Label(root, bg = 'black', fg = 'white', text = 'Title')
title.grid(row = 0, column = 1, columnspan= 4, sticky = 'ew')

b1 = Button(root, bg = 'red', fg = 'white', text = 'Left Button',width = 20)
b2 = Button(root, bg = 'green', fg = 'white',text = 'Very Very Long Text Button',width = 20)
b3 = Button(root, bg = 'blue', fg = 'white', text = 'Right Button',width = 20)

b1.grid(row = 1, column = 1, sticky = 'ew')
b2.grid(row = 1, column = 2, sticky = 'w')
b3.grid(row = 1, column = 3, sticky = 'w')

root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.mainloop()