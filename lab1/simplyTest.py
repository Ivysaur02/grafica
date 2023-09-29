import unittest
from tkinter import *
from main import create_oval, move_oval


class TestOval(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=500, height=500, bg='white')
        self.canvas.pack()
        self.oval = create_oval(self.canvas, 250, 250, 50, 25, 'red')

    def test_create_oval(self):
        self.assertEqual(self.canvas.type(self.oval), 'oval')
        self.assertEqual(self.canvas.coords(self.oval), [200, 225, 300, 275])
        self.assertEqual(self.canvas.itemcget(self.oval, 'fill'), 'red')

    def test_move_oval(self):
        move_oval(self.canvas, self.oval, 'up', 10)
        self.assertEqual(self.canvas.coords(self.oval), [200, 215, 300, 265])
        move_oval(self.canvas, self.oval, 'down', 10)
        self.assertEqual(self.canvas.coords(self.oval), [200, 225, 300, 275])
        move_oval(self.canvas, self.oval, 'left', 10)
        self.assertEqual(self.canvas.coords(self.oval), [190, 225, 290, 275])
        move_oval(self.canvas, self.oval, 'right', 10)
        self.assertEqual(self.canvas.coords(self.oval), [200, 225, 300, 275])

    def tearDown(self):
        self.root.destroy()


if __name__ == '__main__':
    unittest.main()
