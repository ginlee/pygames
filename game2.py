import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE=(640,480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont('arial', 16)
font_height = font.get_linesize()
event_text = []

while True:
	event = pygame.event.wait()
	event_text.append(str(event))
	#get the name of time???
	event_text = event_text[-SCREEN_SIZE[1]//font_height:]
	#this operation to ensure there is only one screen line size words
	#in event_text list

	if event.type == QUIT:
		exit()

	screen.fill((255,255,255))

	y = SCREEN_SIZE[1]-font_height
	#find a appropriate postion to begin, but need to leave one line blank

	for text in reversed(event_text):
		screen.blit(font.render(text, True, (0,0,0)), (0,y))
		y-=font_height

	pygame.display.update()