import numpy
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

FOVY = 45
NEAR = 0.1
FAR = 50.0
ROTATION_SPEED = 1
WAIT_TIME = 10
GL_FRAGMENT_DEPTH = 32
CAMERA = 3
RADIUS_SPHERE = 1


class EarthModel:
    """Класс EarthModel, используемый для создания приложения OpenGL. Показывает вращающуюся сферу с текстурой земли """

    def __init__(self, window_width=800, window_height=600, texture_path="lab5/img/earth_texture.jpg"):
        self.window_width = window_width
        self.window_height = window_height
        self.texture_path = texture_path
        self.angle = 0
        self.init_window()

    def init_window(self):
        """
            Инициализация окна и OpenGL.
        - glEnable(GL_DEPTH_TEST): Включает тест глубины для определения порядка отображения объектов в трехмерном
         пространстве.
        - glEnable(GL_TEXTURE_2D): Включает использование 2D текстур для накладывания изображений на объекты в
         трехмерном пространстве.
        - glMatrixMode(GL_PROJECTION): Устанавливает текущую матрицу как матрицу проекции для определения отображения
         трехмерных объектов на двумерном экране.

         - gluPerspective(FOVY, aspect, NEAR, FAR): Устанавливает матрицу проекции в виде перспективной проекции
                  с заданным углом обзора, соотношением сторон и ближней и дальней плоскостями отсечения.
        - gluLookAt(eye_x, eye_y, eye_z, center_x, center_y, center_z, up_x, up_y, up_z): Устанавливает положение и
             ориентацию камеры в трехмерном пространстве.
        """

        pygame.init()
        pygame.display.set_mode((self.window_width, self.window_height), pygame.DOUBLEBUF | pygame.OPENGL)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(FOVY, (self.window_width / self.window_height), NEAR, FAR)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def load_texture(self):
        """Загрузка текстуры."""
        # Загрузка изображения из файла с использованием библиотеки PIL
        img = Image.open(self.texture_path)
        img_data = numpy.array(list(img.getdata()), numpy.uint8)
        # Генерация идентификатора текстуры
        texture = glGenTextures(1)
        # Привязка текстуры к идентификатору
        glBindTexture(GL_TEXTURE_2D, texture)
        # Установка параметров фильтрации текстуры
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        # Загрузка изображения в текстуру
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
        return texture

    def draw_sphere(self, radius, texture):
        """Отрисовка сферы с текстурой."""
        glPushMatrix()
        # Поворот сферы на угол self.angle вокруг оси Z
        glRotatef(self.angle, 0, 0, 1)
        # Привязка текстуры к сфере
        glBindTexture(GL_TEXTURE_2D, texture)
        # Создание нового квадрика для отрисовки сферы
        quad = gluNewQuadric()
        # Включение наложения текстуры на квадрик
        gluQuadricTexture(quad, GL_TRUE)
        # Отрисовка сферы с помощью квадрика
        gluSphere(quad, radius, GL_FRAGMENT_DEPTH, GL_FRAGMENT_DEPTH)
        # Удаление квадрика после отрисовки сферы
        gluDeleteQuadric(quad)
        # Восстановление предыдущей матрицы
        glPopMatrix()

    def handle_events(self):
        """Обработка событий клавиатуры."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

    def main_loop(self):
        """Основной цикл приложения."""
        texture = self.load_texture()
        while True:
            self.handle_events()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            gluLookAt(-CAMERA, -CAMERA, 0,  # Положение камеры (x, y, z)
                      0, 0, 0,  # Точка, на которую направлена камера (x, y, z)
                      0, 0, -CAMERA)  # Направление "вверх" для камеры (x, y, z)
            self.draw_sphere(RADIUS_SPHERE, texture)
            self.angle += ROTATION_SPEED
            pygame.display.flip()
            pygame.time.wait(WAIT_TIME)


if __name__ == '__main__':
    earth = EarthModel()
    earth.main_loop()
