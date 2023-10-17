from tkinter import Tk, Canvas, Label, Toplevel, Menu


class Ball:
    def __init__(self, canvas, x, y, vx, vy, radius, color):
        """
        Класс, представляющий абсолютно упругий шарик.

        Атрибуты:
        canvas (Canvas): холст, на котором отображается шарик.
        x (int): координата x центра шарика.
        y (int): координата y центра шарика.
        vx (int): скорость шарика по оси x.
        vy (int): скорость шарика по оси y.
        r (int): радиус шарика.
        color (str): цвет шарика.

        Методы:
        __init__(self, canvas, x, y, vx, vy, r, color): создает новый объект класса Ball.
        move(self): перемещает шарик на холсте в соответствии со скоростью.
        collide(self, x1, y1, x2, y2): обрабатывает столкновения шарика со стенками прямоугольной области.
        """
        self.canvas = canvas
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color
        self.ball = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)

    def move(self):
        """
        Перемещает мячик на холсте в соответствии со скоростью.

        """
        self.x += self.vx
        self.y += self.vy
        self.canvas.move(self.ball, self.vx, self.vy)

    def collide(self, x1, y1, x2, y2):
        """
        Проверяет, столкнулся ли мячик со стенками прямоугольной области, и изменяет его скорость при необходимости.

        :param x1: координата x левой стенки
        :param y1: координата y верхней стенки
        :param x2: координата x правой стенки
        :param y2: координата y нижней стенки
        """
        if self.x - self.radius <= x1 or self.x + self.radius >= x2:
            self.vx = -self.vx
        if self.y - self.radius <= y1 or self.y + self.radius >= y2:
            self.vy = -self.vy


def update(canvas, ball, x1, y1, x2, y2):
    """
    Обновляет положение мячика на холсте и проверяет столкновения со стенками.

    :param canvas: холст, на котором нарисован мячик
    :param ball: объект мячика
    :param x1: координата x левой стенки
    :param y1: координата y верхней стенки
    :param x2: координата x правой стенки
    :param y2: координата y нижней стенки
    """
    ball.move()
    ball.collide(x1, y1, x2, y2)
    canvas.after(10, update, canvas, ball, x1, y1, x2, y2)


def on_click(event):
    """
    Создает новый объект мячика при щелчке левой кнопкой мыши на холсте.

    :param event: событие щелчка левой кнопкой мыши
    """
    ball = Ball(canvas, event.x, event.y, vx, vy, radius, color)
    canvas.bind('<Button-1>', lambda event: None)
    canvas.after(10, update, canvas, ball, x1, y1, x2, y2)


def get_user_input():
    """
    Запрашивает у пользователя размеры canvas, скорость движения мячика и его цвет.

    :return: кортеж значений, содержащий размеры canvas, скорость движения мячика и его цвет
    """
    canvas_width, canvas_height = input("Введите размеры Canvas (ширина и высота) через пробел: ").split()
    canvas_width = int(canvas_width) if canvas_width else 400
    canvas_height = int(canvas_height) if canvas_height else 400

    vx, vy = input("Введите скорость движения мячика (например, '1 1'): ").split()
    vx = int(vx) if vx else 1
    vy = int(vy) if vy else 1

    color = input("Введите цвет мячика (например, 'red' или '#FF0000'): ") or 'red'

    radius = int(input("Введите радиус мячика: ") or 10)

    return canvas_width, canvas_height, vx, vy, color, radius


def open_help_window():
    """
    Открывает модальное окно с содержимым файла help.txt.
    """
    with open("util/help.txt") as f:
        help_text = f.read()
    help_window = Toplevel(root)
    help_window.title("Справка")
    help_window.geometry("400x300")
    help_window.grab_set()
    help_label = Label(help_window, text=help_text)
    help_label.pack()
    help_window.wait_window()


def open_version_window():
    """
    Открывает модальное окно с версией программы.
    """
    with open("util/version.txt") as f:
        version_text = f.read()
    version_window = Toplevel(root)
    version_window.title("Версия программы")
    version_window.geometry("200x100")
    version_window.grab_set()
    version_label = Label(version_window, text=version_text)
    version_label.pack()
    version_window.wait_window()


if __name__ == "__main__":
    canvas_width, canvas_height, vx, vy, color, radius = get_user_input()

    root = Tk()

    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    menubar = Menu(root)
    root.config(menu=menubar)

    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="Справка", command=open_help_window)
    menubar.add_cascade(label="Справка", menu=help_menu)

    version_menu = Menu(menubar, tearoff=0)
    version_menu.add_command(label="Версия", command=open_version_window)
    menubar.add_cascade(label="О программе", menu=version_menu)

    x1, y1, x2, y2 = 0, 0, canvas_width, canvas_height
    canvas.create_line(x1, y1, x2, y1, x2, y2, x1, y2, x1, y1)

    canvas.bind('<Button-1>', on_click)
    root.title("Lab 2")

    root.mainloop()
