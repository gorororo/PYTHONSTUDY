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

#이동거리
to_x = 0
to_y = 0

# 몬스터 설정
monsterPath = ['resources/monster01.png', 'resources/monster02.png', 'resources/monster03.png', 'resources/monster04.png', \
                'resources/monster05.png', 'resources/monster06.png', 'resources/monster07.png', 'resources/monster08.png', \
                'resources/monster09.png', 'resources/monster10.png']
monster = pygame.image.load(random.choice(monsterPath))
monster_size = monster.get_rect().size 
monster_width = monster_size[0]
monster_height = monster_size[1]
monster_x_pos = 0
monster_y_pos = random.randint(0, int(screen_width*0.3)) 
monster_speed = random.randint(1,5)



#게임진행
while running :

#초당 프레임 설정
    pygame.time.Clock().tick(60)
#이벤트처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 방향키가 눌러졌는지 확인
    if event.type == pygame.KEYDOWN : 
        if event.key == pygame.K_LEFT : to_x -=5
        elif event.key == pygame.K_RIGHT : to_x +=5
        elif event.key == pygame.K_DOWN : to_y +=5 
        elif event.key == pygame.K_UP : to_y -=5

    # 방향키를 떼면
    if event.type == pygame.KEYUP : 
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :\
        to_x, to_y = 0,0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN : \
        to_x, to_y = 0, 0 

#우주선 위치 설정
    spaceship_x_pos += to_x
    spaceship_y_pos += to_y

#우주선 스크린 안에서 움직이도록 처리
    if spaceship_x_pos < 0 :
        spaceship_x_pos = 0
    elif spaceship_x_pos > screen_width - spaceship_width :
        spaceship_x_pos = screen_width - spaceship_width

    if spaceship_y_pos <screen_height/2:
        spaceship_y_pos = screen_width/2
    elif spaceship_y_pos > screen_height - spaceship_height:
        spaceship_y_pos = screen_height - spaceship_height

#몬스터가 왼쪽에서 오른쪽으로 이동
    monster_x_pos +=monster_speed
    if monster_x_pos > screen_width :
        monster_x_pos = 0
        monster_y_pos = random.randint(0, int(screen_width*0.3))
        monster = pygame.image.load(random.choice(monsterPath))
        monster_speed = random.randint(1,5)



#화면에 그리기
    screen.fill((r,g,b))
    screen.blit(spaceship,(spaceship_x_pos,spaceship_y_pos))
    screen.blit(monster,(monster_x_pos,monster_y_pos))
    pygame.display.update()

pygame.quit()