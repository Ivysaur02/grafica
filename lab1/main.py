from tkinter import *


def create_oval(canvas, x, y, a, b, color):
    """
    Создает овальную фигуру на холсте с заданными координатами и цветом.

    Аргументы:
        canvas (Canvas): Холст, на котором создается овальная фигура.
        x (int): X-координата центра овала.
        y (int): Y-координата центра овала.
        a (int): Полуось a овала.
        b (int): Полуось b овала.
        color (str): Цвет заливки овала.

    Возвращает:
        int: Идентификатор нового объекта овала на холсте.
    """
    x0 = x - a
    y0 = y - b
    x1 = x + a
    y1 = y + b
    return canvas.create_oval(x0, y0, x1, y1, fill=color)


def move_oval(canvas, oval, direction, distance):
    """
    Перемещает овальную фигуру на холсте в заданном направлении.

    Аргументы:
        canvas (Canvas): Холст, на котором находится овальная фигура.
        oval (int): Идентификатор объекта овала на холсте.
        direction (str): Направление, в котором нужно переместить овальную фигуру ("up", "down", "left" или "right").
        distance (int): Расстояние, на которое нужно переместить овальную фигуру.
    """
    if direction == "up":
        canvas.move(oval, 0, -distance)
    elif direction == "down":
        canvas.move(oval, 0, distance)
    elif direction == "left":
        canvas.move(oval, -distance, 0)
    elif direction == "right":
        canvas.move(oval, distance, 0)


def bind_keys(canvas, oval, colors, root, a, b):
    """
    Привязывает клавиши со стрелками, "Next", "Prior" и "Escape" к соответствующим функциям.

    Аргументы:
        canvas (Canvas): Холст, на котором находится овальная фигура.
        oval (int): Идентификатор объекта овала на холсте.
        colors (list): Список цветов заливки для овала.
        root (Tk): Корневое окно приложения.
        a (int): Полуось a овала.
        b (int): Полуось b овала.
    """
    current_index = 0

    def change_color(event):
        nonlocal current_index
        if event.keysym == 'Next':
            current_index = (current_index + 1) % len(colors)
        elif event.keysym == 'Prior':
            current_index = (current_index - 1) % len(colors)
        next_color = colors[current_index]
        canvas.itemconfig(oval, fill=next_color)

    canvas.bind('<Up>', lambda event: move_oval(canvas, oval, "up", a / 2))
    canvas.bind('<Down>', lambda event: move_oval(canvas, oval, "down", a / 2))
    canvas.bind('<Left>', lambda event: move_oval(canvas, oval, "left", b / 2))
    canvas.bind('<Right>', lambda event: move_oval(canvas, oval, "right", b / 2))
    canvas.bind('<Next>', change_color)
    canvas.bind('<Prior>', change_color)
    canvas.bind("<Escape>", lambda event: root.destroy())


def get_oval_coordinates():
    """
    Запрашивает у пользователя координаты и полуоси овала и возвращает их в виде кортежа.

    Возвращает:
        tuple: X-координата, Y-координата, полуось a и полуось b овала.
    """
    x = int(input("Введите X-координату центра: "))
    y = int(input("Введите Y-координату центра: "))
    a = int(input("Введите полуось a: "))
    b = int(input("Введите полуось b: "))
    return x, y, a, b


def main():
    """
    Инициализирует холст, создает овальную фигуру, привязывает клавиши и запускает главный цикл.
    """
    colors = ['red', 'green', 'blue', 'yellow', 'pink', 'purple']
    x, y, a, b = get_oval_coordinates()

    root = Tk()
    canvas = Canvas(width=500, height=500, bg='white')
    canvas.focus_set()
    canvas.pack()

    oval = create_oval(canvas, x, y, a, b, colors[0])
    bind_keys(canvas, oval, colors, root, a, b)

    root.mainloop()


if __name__ == "__main__":
    main()
