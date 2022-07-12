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

#우주선 설정
spaceship = pygame.image.load('resources/ship02.png')
spaceship_size = spaceship.get_rect().size
spaceship_width = spaceship_size[0] #가로 사이즈
spaceship_height = spaceship_size[1] #세로 사이즈
spaceship_x_pos = (screen_width/2) - (spaceship_width/2)# 정중앙
spaceship_y_pos = screen_height*0.8 #세로크기*0.8

#게임진행
while running :
#이벤트처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#화면에 그리기
    screen.fill((r,g,b))
    screen.blit(spaceship,(spaceship_x_pos,spaceship_y_pos))
    pygame.display.update()

pygame.quit()