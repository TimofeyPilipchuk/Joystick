import pygame
import pygame as pg
import random
from settings import *
from classes import *


pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN | pg.SCALED)
pg.display.set_caption("Zombie")

clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
istouch = False
while running:
    # Обработка кадров

    clock.tick(FPS)
    mouse = pg.mouse.get_pos()
    # Обработка процессов(событий)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

            elif event.key == pg.K_w:
                player.rect.centery -= 5

        if event.type == pg.MOUSEBUTTONDOWN:  # Если мышь\палец нажата
            istouch = True  # Присваиваем истину
        # MOUSE2 = mouse

        elif event.type == pg.MOUSEBUTTONUP:  # Если мышь\палец отпускаются
            istouch = False  # Присваиваем ложь

    joy_pos = MOUSE2
    if istouch:  # Если мышь\палец нажаты
        cur_mouse = mouse[0] - MOUSE2[0], mouse[1] - MOUSE2[
            1]  # Определяем позицию мыши\пальца относительно середины джойстика
        angler = math.atan2(cur_mouse[0],
                            cur_mouse[1])  # Определяем угол курсора джойстка относительно середины джойстика в радианах
        distance = math.sqrt(pow(cur_mouse[0], 2) + pow(cur_mouse[1],
                                                        2))  # Определяем расстояние от середины джойсткеа до курсора джойстка
        if TOUCH_RADIUS * 4.2 < distance:
            joy_pos = MOUSE2
            player.speedx = 0
            player.speedy = 0

        else:
            if distance > 80:  # Если расстояние от середины джойстика до курсора джойстика больше 80
                si = math.sin(angler)  # Определяем синус угла курсора относительно середины джойстика
                co = math.cos(angler)  # Определяем косинус угла курсора относительно середины джойстика
                joy_pos = (math.degrees(si) * 1.4 + MOUSE2[0], math.degrees(co) * 1.4 + MOUSE2[
                    1])  # устанавливаем позицию курсора джойстика с множителем 1.4
                distance = 80  # Устанавливаем расстояние до курсора джойстка относительно середины джойсткка 80

            else:
                joy_pos = mouse

            player.speedx = math.sin(angler) * distance / 9
            player.speedy = math.cos(angler) * distance / 9

    else:
        player.speedx = 0
        player.speedy = 0
    screen.fill(BLACK)
    pg.draw.circle(screen, (100, 100, 100), MOUSE2, TOUCH_RADIUS)  # Рисуем круг в нажатом фиксированом месте
    pg.draw.circle(screen, (234, 234, 234), joy_pos,
                   TOUCH_RADIUS // 2)  # Рисуем курсор джойстика на экране по позиции переменной joy_pos

    # Обновление
    all_sprites.update()

    # Визуализация
    all_sprites.draw(screen)

    # Рендинг

    pg.display.flip()

pg.quit()