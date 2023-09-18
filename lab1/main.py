from tkinter import *

colors = ['red', 'green', 'blue', 'yellow', 'pink','purple' ]
current_index = 0

def change_color(event):
    global current_index
    if event.keysym == 'Next':
        current_index = (current_index + 1) % len(colors)
    elif event.keysym == 'Prior':
        current_index = (current_index - 1) % len(colors)
    next_color = colors[current_index]
    c.itemconfig(ball, fill=next_color)


def hello():
    print('hello')

root = Tk()
c = Canvas(width=300, height=300, bg='white')
c.focus_set()
c.pack()

ball = c.create_oval(140, 140, 160, 160, fill='red')
c.bind('<Up>', lambda event: c.move(ball, 0, -2))
c.bind('<Down>', lambda event: c.move(ball, 0, 2))
c.bind('<Left>', lambda event: c.move(ball, -2, 0))
c.bind('<Right>', lambda event: c.move(ball, 2, 0))
c.bind('<Next>', change_color)
c.bind('<Prior>', change_color)
root.bind("<Escape>", lambda event: root.destroy())


root.mainloop()