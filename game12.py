background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

backgroun = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

#clock objuct
clock = pygame.time.Clock()

x = 0.
#speed (pixel/sec)
speed = 250.

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	screen.blit(backgroun, (0,0))
	screen.blit(sprite, (x, 100))

	time_passed = clock.tick()
	time_passed_seconds = time_passed/1000.0

	distance_moved = time_passed_seconds * speed
	x += distance_moved

	#think whats the different for minusing 640 and reset
	if x > 640.:
		x -= 640.
	pygame.display.update()