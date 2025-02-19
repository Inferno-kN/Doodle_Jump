import pygame
import sys
from Doodlik import Doodle

#Цвета
WHITE = 255, 255, 255
BLACK = 0, 0, 0


def run():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Лютый джамп")
    doodle = Doodle(screen)


    while True:
        for event in pygame.event.get(): #получаем события пользователя
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(WHITE) #установили белый фон
        doodle.output() # отрисовка на главный экран нашего дудлика
        pygame.display.flip() # обновление экрана



run()
