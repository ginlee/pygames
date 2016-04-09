#-*- coding: utf-8 -*-
#remember the line above is necessary and the code shoule be same with the file
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,480), 0, 32)

#font = pygame.font.SysFont("宋体", 40)
#the above line is available on linux machine
#font = pygame.font.SysFont("apple", 40)
#use get_fonts() to see whats your sys font on your machine
font = pygame.font.Font("SimSun.ttf", 40)
text_surface = font.render(u"你好", True, (0,255,0))

x = 0;
y = (480 - text_surface.get_height())/2

background = pygame.image.load("sushiplate.jpg").convert()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	screen.blit(background, (0,0))

	x -= 2 #the caption move velocity
	if x < -text_surface.get_width():
		x = 640 - text_surface.get_width()

	screen.blit(text_surface, (x,y))

	pygame.display.update()