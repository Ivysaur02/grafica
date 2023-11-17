import unittest

import pygame

from earchWithOpenGL import EarthModel


class TestEarthModel(unittest.TestCase):
    def setUp(self):
        self.earth = EarthModel()

    def test_init_window(self):
        """Проверяет корректную инициализацию окна."""
        self.earth.init_window()
        self.assertIsNotNone(pygame.display.get_surface(), "Окно не было создано")
        self.assertEqual(pygame.display.get_surface().get_width(), self.earth.window_width, "Некорректная ширина окна")
        self.assertEqual(pygame.display.get_surface().get_height(), self.earth.window_height,
                         "Некорректная высота окна")

    def test_load_texture(self):
        """Проверяет корректную загрузку текстуры."""
        texture = self.earth.load_texture("earth_texture.jpg")
        self.assertIsNotNone(texture, "Текстура не была загружена")

    def test_draw_sphere(self):
        """Проверяет корректную отрисовку сферы."""
        texture = self.earth.load_texture("earth_texture.jpg")
        self.earth.draw_sphere(1, texture)
        self.assertIsNotNone(pygame.display.get_surface(), "Окно не было создано")
        self.assertIsNotNone(
            pygame.display.get_surface().get_at((self.earth.window_width // 2, self.earth.window_height // 2)),
            "Сфера не была отрисована")

    def test_handle_events(self):
        """Проверяет обработку событий клавиатуры."""
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)
        pygame.event.post(event)
        self.earth.handle_events()
        self.assertFalse(pygame.get_init(), "Окно не было закрыто после нажатия ESC")


if __name__ == '__main__':
    unittest.main()
