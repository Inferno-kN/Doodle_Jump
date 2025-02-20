import pygame
import sys
from Doodlik import Doodle

#Цвета
WHITE = 255, 255, 255
BLACK = 0, 0, 0
FPS = 90


def run():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Лютый джамп")
    doodle = Doodle(screen)
    clock = pygame.time.Clock()


    while True:
        clock.tick(FPS)
        for event in pygame.event.get(): #получаем события пользователя (по типу нажал на клавишу и тд)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE) #установили белый фон
        doodle.output() # отрисовка на главный экран нашего дудлика
        pygame.display.flip() # обновление экрана
        clock.tick(FPS) #ставим ограничение на фпс до 90

run()
