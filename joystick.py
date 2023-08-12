import pygame as pg 		#импотрируем главную библиотеку для отрисовки интерфейса
import math		#Импортируем модуль для математических операций
from settings import *


pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN | pg.SCALED)	#Создаем окно размером 800 на 480 пикселей
clock = pg.time.Clock()	

istouch = False		#Создаем переменную чтобы знать нажата мышь\палец или нет
# MOUSE2 = (-1000, -1000)		#Переменная для фиксированого значения мыши

playerX = 200
playerY = 200


while 1:
	screen.fill((0, 0, 0))		#Закрашиваем окно в черный цвет
	mouse = pg.mouse.get_pos()		#Определяем позицию мыши\пальца
	for ev in pg.event.get():
		if ev.type == pg.QUIT:		#Проверяем на выход из окна
			exit()

		if ev.type == pg.MOUSEBUTTONDOWN:		#Если мышь\палец нажата
			istouch = True		#Присваиваем истину
			# MOUSE2 = mouse

		elif ev.type == pg.MOUSEBUTTONUP:		#Если мышь\палец отпускаются
			istouch = False		#Присваиваем ложь

	joy_pos = MOUSE2
	if istouch:		#Если мышь\палец нажаты
		cur_mouse = mouse[0] - MOUSE2[0], mouse[1] - MOUSE2[1]		#Определяем позицию мыши\пальца относительно середины джойстика
		angler = math.atan2(cur_mouse[0], cur_mouse[1])		#Определяем угол курсора джойстка относительно середины джойстика в радианах
		distance = math.sqrt(pow(cur_mouse[0], 2) + pow(cur_mouse[1], 2))		#Определяем расстояние от середины джойсткеа до курсора джойстка
		if TOUCH_RADIUS * 4.2 < distance:
			joy_pos = MOUSE2

		else:
			if distance > 80:		#Если расстояние от середины джойстика до курсора джойстика больше 80
				si = math.sin(angler)		#Определяем синус угла курсора относительно середины джойстика
				co = math.cos(angler)		#Определяем косинус угла курсора относительно середины джойстика
				joy_pos = (math.degrees(si)*1.4+MOUSE2[0], math.degrees(co)*1.4+MOUSE2[1])		#устанавливаем позицию курсора джойстика с множителем 1.4
				distance = 80		#Устанавливаем расстояние до курсора джойстка относительно середины джойсткка 80

			else:
				joy_pos = mouse

			playerX += math.sin(angler)*distance/20
			playerY += math.cos(angler)*distance/20
	pg.draw.circle(screen, (100, 100, 100), MOUSE2, TOUCH_RADIUS)  # Рисуем круг в нажатом фиксированом месте
	pg.draw.circle(screen, (234, 234, 234), joy_pos, TOUCH_RADIUS // 2)  # Рисуем курсор джойстика на экране по позиции переменной joy_pos
	pg.draw.circle(screen, (20, 200, 20), (playerX, playerY), 50)

	clock.tick(60)			#Ограничиваем кадры в секунду до 60
	pg.display.update()		#Обновляем поверхность экрана