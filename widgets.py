from tkinter import *
root = Tk()

stringvars = []
answers = []

result = StringVar()
result.set("0")


def check_answers():
    points = 0
    for i in range(len(answers)):
        if stringvars[i].get() == answers[i]:
            points += 1
    result.set(str(points))


f1 = Frame(root,padx=10, pady=10, bg = 'red')
f1.pack()
sample1 = Label(f1, text="There were some people on a train. 19 people get off the train at the first stop. 17 people get on the train. Now there are 63 people on the train. How many people were on the train to begin with?")
sample1.pack()
g1 = StringVar()
ra = Radiobutton(f1, text="98",variable=g1, value="0")
ra.pack()
rb = Radiobutton(f1, text="100",variable=g1, value="1")
rb.pack()
rc = Radiobutton(f1, text="65",variable=g1, value="2")
rc.pack()

answers.append("2")
stringvars.append(g1)

f2 = Frame(root,padx=10, pady=10, bg = 'orange')
f2.pack()
sample2 = Label(f2, text="6÷2(1+2)=?")
sample2.pack()
g2 = StringVar()
rd = Radiobutton(f2, text="5",variable=g2, value="0")
rd.pack()
re = Radiobutton(f2, text="10",variable=g2, value="1")
re.pack()
rf = Radiobutton(f2, text="9",variable=g2, value="2")
rf.pack()

answers.append("2")
stringvars.append(g2)

f3 = Frame(root,padx=10, pady=10, bg = 'yellow')
f3.pack()
sample3 = Label(f3, text="(18495×5858465)÷12594-25416+5525×123÷2×0=?")
sample3.pack()
g3 = StringVar()
rg = Radiobutton(f3, text="0",variable=g3, value="0")
rg.pack()
rh = Radiobutton(f3, text="8578070.59481", variable=g3, value="1")
rh.pack()
ri = Radiobutton(f3, text="4736389", variable=g3, value="2")
ri.pack()

answers.append("1")
stringvars.append(g3)

f4 = Frame(root,padx=10, pady=10, bg = 'green')
f4.pack()
sample4 = Label(f4, text="9+10=?")
sample4.pack()
g4 = StringVar()
rj = Radiobutton(f4, text="21",variable=g4, value="0")
rj.pack()
rk = Radiobutton(f4, text="19",variable=g4, value="1")
rk.pack()
rl = Radiobutton(f4, text="20", variable=g4, value="2")
rl.pack()

answers.append("1")
stringvars.append(g4)

f5 = Frame(root,padx=10, pady=10, bg = 'blue')
f5.pack()
sample5 = Label(f5, text="8÷2(2+2)=?")
sample5.pack()
g5 = StringVar()
rm = Radiobutton(f5, text="16",variable=g5, value="0")
rm.pack()
rn = Radiobutton(f5, text="20",variable=g5, value="1")
rn.pack()
ro = Radiobutton(f5, text="15",variable=g5, value="2")
ro.pack()

answers.append("0")
stringvars.append(g5)



submitButton = Button(root, text='Submit Answers',bg='white', command=check_answers)
submitButton.pack()
results = Label(root, textvariable=result)
results.pack()

root.mainloop()
