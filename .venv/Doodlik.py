import pygame

class Doodle:

    def __init__(self, screen):
        #здесь будет инициализация нашего дудлика
        self.screen = screen
        self.image = pygame.image.load("images/doodlik.png")  # загрузка нашего дудлика на экран
        self.rectangle = self.image.get_rect()  # получение картинки как прямоугольник
        self.screen_rectangle = screen.get_rect()
        self.rectangle.centerx = self.screen_rectangle.centerx
        self.rectangle.bottom = self.screen_rectangle.bottom

        # теперь обозначим параметры движения у дудлика
        self.speed = 5
        self.gravity = 0.5






