import unittest
from unittest.mock import patch
from tkinter import Tk, Canvas
from elastic_ball import Ball, update, on_click, get_user_input


class TestBall(unittest.TestCase):
    """
        Класс, содержащий тесты для класса Ball.

        Методы:
        setUp(self): создает объект мячика для тестов.
        test_move(self): проверяет, что метод move класса Ball корректно перемещает мячик.
        test_collide(self): проверяет, что метод collide класса Ball корректно обрабатывает столкновения мячика со стенками
         прямоугольной области.
        """

    def setUp(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.ball = Ball(self.canvas, 50, 50, 1, 1, 10, 'red')

    def test_move(self):
        self.ball.move()
        self.assertEqual(self.ball.x, 51)
        self.assertEqual(self.ball.y, 51)

    def test_collide_left_wall(self):
        # Test collision with left wall
        self.ball.x = 10
        self.ball.vx = -1
        self.ball.collide(0, 0, 400, 400)
        self.assertEqual(self.ball.vx, 1)

    def test_collide_right_wall(self):
        # Test collision with right wall
        self.ball.x = 390
        self.ball.vx = 1
        self.ball.collide(0, 0, 400, 400)
        self.assertEqual(self.ball.vx, -1)

    def test_collide_top_wall(self):
        # Test collision with top wall
        self.ball.y = 10
        self.ball.vy = -1
        self.ball.collide(0, 0, 400, 400)
        self.assertEqual(self.ball.vy, 1)

    def test_collide_bottom_wall(self):
        # Test collision with bottom wall
        self.ball.y = 390
        self.ball.vy = 1
        self.ball.collide(0, 0, 400, 400)
        self.assertEqual(self.ball.vy, -1)


class TestGetUserInput(unittest.TestCase):
    """
        Класс, содержащий тесты для функции get_user_input.

        Методы:
        test_user_input(self, mock_input): проверяет, что функция get_user_input возвращает корректные значения при заданных входных данных.
        """

    @patch('builtins.input', side_effect=['500 500', '2 2', 'blue', '20'])
    def test_user_input(self, mock_input):
        """
        Проверяет, что функция get_user_input возвращает корректные значения при заданных входных данных.

        Аргументы:
        mock_input: мок объект для имитации ввода данных пользователем.

        Проверяет, что функция возвращает корректные значения при заданных входных данных.
        """
        canvas_width, canvas_height, vx, vy, color, radius = get_user_input()
        self.assertEqual(canvas_width, 500)
        self.assertEqual(canvas_height, 500)
        self.assertEqual(vx, 2)
        self.assertEqual(vy, 2)
        self.assertEqual(color, 'blue')
        self.assertEqual(radius, 20)
