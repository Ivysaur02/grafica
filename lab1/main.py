from tkinter import *

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'purple']
current_index = 0


def change_color(event):
    global current_index
    if event.keysym == 'Next':
        current_index = (current_index + 1) % len(colors)
    elif event.keysym == 'Prior':
        current_index = (current_index - 1) % len(colors)
    next_color = colors[current_index]
    c.itemconfig(ball, fill=next_color)


root = Tk()
c = Canvas(width=500, height=500, bg='white')
c.focus_set()
c.pack()

x = int(input("Enter the x-coordinate of the center: "))
y = int(input("Enter the y-coordinate of the center: "))
a = int(input("Enter the semi-axis a: "))
b = int(input("Enter the semi-axis b: "))

x0 = x - a
y0 = y - b
x1 = x + a
y1 = y + b

ball = c.create_oval(x0, y0, x1, y1, fill='red')

c.bind('<Up>', lambda event: c.move(ball, 0, -(a / 2)))
c.bind('<Down>', lambda event: c.move(ball, 0, (a / 2)))
c.bind('<Left>', lambda event: c.move(ball, -(b / 2), 0))
c.bind('<Right>', lambda event: c.move(ball, (b / 2), 0))
c.bind('<Next>', change_color)
c.bind('<Prior>', change_color)
root.bind("<Escape>", lambda event: root.destroy())

root.mainloop()
