import pygame
import random

pygame.init()  # 초기화

# 화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면타이틀 설정
pygame.display.set_caption('우주괴물 무찌르기')

# 게임상태
running = True

# 배경색깔 랜덤으로 표시하기
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

# 우주선 설정
spaceship = pygame.image.load('resources/ship02.png')
spaceship_size = spaceship.get_rect().size
spaceship_width = spaceship_size[0]
spaceship_height = spaceship_size[1]
spaceship_x_pos = (screen_width/2) - (spaceship_width/2)
spaceship_y_pos = screen_height*0.8

# 우주선 이동거리(좌표)
to_x = 0
to_y = 0

# 몬스터 설정
monsterPath = ['resources/monster01.png', 'resources/monster02.png', 'resources/monster03.png', 'resources/monster04.png',
               'resources/monster05.png', 'resources/monster06.png', 'resources/monster07.png', 'resources/monster08.png',
               'resources/monster09.png', 'resources/monster10.png']
monster = pygame.image.load(random.choice(monsterPath))
monster_size = monster.get_rect().size
monster_width = monster_size[0]
monster_height = monster_size[1]
monster_x_pos = 0
monster_y_pos = random.randint(0, int(screen_width*0.3))
monster_speed = random.randint(1, 5)

# 미사일 설정
missile = pygame.image.load('./resources/missile.png')
missile_size = missile.get_rect().size
missile_x_pos = None
missile_y_pos = None

# 맞힌 몬스터 숫자를 저장
firecount = 0

# 폰트정의(기본폰트, 30)
game_font = pygame.font.Font(None, 30)

# 게임진행
while running:
    # 초당 프레임 설정하기
    pygame.time.Clock().tick(50)

    # 이벤트 처리
    for event in pygame.event.get():
        # 창이 닫히는 이벤트가 발생하였는가
        if event.type == pygame.QUIT:
            running = False

        # 방향키가 눌러졌는지 확인
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

            # 스페이스 바를 누르면 우주선 위치로 미사일 위치 변경
            elif event.key == pygame.K_SPACE:
                if missile_x_pos == None:
                    missile_x_pos = spaceship_x_pos + \
                        (spaceship_width/2)-(missile_size[0]/2)
                    missile_y_pos = spaceship_y_pos

        # 방향키를 떼면 멈춤
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x, to_y = 0, 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_x, to_y = 0, 0

    # 우주선 위치  설정
    spaceship_x_pos += to_x
    spaceship_y_pos += to_y

    # 우주선이 스크린 안에서 움직이도록 처리
    if spaceship_x_pos < 0:
        spaceship_x_pos = 0
    elif spaceship_x_pos > screen_width - spaceship_width:
        spaceship_x_pos = screen_width - spaceship_width

    if spaceship_y_pos < screen_height/2:
        spaceship_y_pos = screen_height/2
    elif spaceship_y_pos > screen_height - spaceship_height:
        spaceship_y_pos = screen_height - spaceship_height

    # 몬스터가 왼쪽에서 오른쪽으로 이동
    monster_x_pos += monster_speed
    if monster_x_pos > screen_width:
        monster_x_pos = 0
        monster_y_pos = random.randint(0, int(screen_width*0.3))
        monster = pygame.image.load(random.choice(monsterPath))
        monster_speed = random.randint(1, 5)

    if missile_x_pos != None:
        # 몬스터 미사일에 맞았는지 체크한다.
        if ((monster_x_pos < missile_x_pos) and (missile_x_pos < monster_x_pos + monster_width)) and \
                ((monster_y_pos < missile_y_pos) and (missile_y_pos < monster_y_pos + monster_height)):
            firecount += 1

            # 우주괴물을 초기화(무작위 이미지로 다시 준비)
            monster = pygame.image.load(random.choice(monsterPath))
            monster_size = monster.get_rect().size
            monster_x_pos = 0
            monster_y_pos = random.randint(0, int(screen_width * 0.3))
            monster_speed = random.randint(1, 5)

        missile_y_pos -= 10
        # 미사일이 위로 이동
        if missile_y_pos < 0:
            missile_x_pos, missile_y_pos = None, None  # 총알 사라짐

    # 화면에 그리기
    screen.fill((r, g, b))  # 랜덤으로 배경 정하기
    screen.blit(spaceship, (spaceship_x_pos, spaceship_y_pos))
    screen.blit(monster, (monster_x_pos, monster_y_pos))
    # 미사일을 쏘면
    if missile_x_pos != None:
        screen.blit(missile, (missile_x_pos, missile_y_pos))

    # 점수출력
    txt = game_font.render(f'score : {firecount}', True, (255, 255, 255))
    screen.blit(txt, (10, screen_height-40))

    pygame.display.update()  # 화면 업데이트

# pygame  종료
pygame.quit()
