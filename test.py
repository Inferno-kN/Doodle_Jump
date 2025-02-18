import pygame
import sys

#инициализация pygame
pygame.init()

#Настройки Экрана
width, height = 1000, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Doodle Jump")

#Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #логика игры
    screen.fill(WHITE)


    #Обновление экрана
    pygame.display.flip()

#Завершение игры
pygame.quit()
sys.exit()
