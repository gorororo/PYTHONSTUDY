import pygame
import random

pygame.init()
#화면 크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
#화면타이틀
pygame.display.set_caption('우주괴물 무찌르기')

running = True

# 배경화면 랜덤으로 표시하기
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

while running :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((r,g,b))
    pygame.display.update()

pygame.quit()