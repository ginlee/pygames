#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit
from random import *
from math import pi

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
points = []

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			#press down any keys could reset the screen
			points = []
			screen.fill((255, 255, 255))
		if event.type == MOUSEBUTTONDOWN:
			screen.fill((255, 255, 255))
			#sketch a random rectangle
			random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
			random_pos = ((randint(0, 639), randint(0, 479)))
			random_stop = (639-randint(random_pos[0], 639), 479-randint(random_pos[1], 479))
			pygame.draw.rect(screen, random_color, Rect(random_pos, random_stop))
			#sketch a random circle
			random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
			random_pos = ((randint(0, 639), randint(0, 479)))
			random_radius = randint(1, 200)
			pygame.draw.circle(screen, random_color, random_pos, random_radius)
			#get the current mouse position
			x, y = pygame.mouse.get_pos()
			points.append((x, y))
			#draw an arc following the points
			angle = (x/639.)*pi*2
			pygame.draw.arc(screen, (0,0,0), (0,0,639,479), 0, angle, 3)
			#eclipse
			pygame.draw.ellipse(screen, (0, 255, 0), (0, 0 ,x, y))
			#sketch two lines to internect at the click position
			pygame.draw.line(screen, (0,0,255), (0,0), (x, y))
			pygame.draw.line(screen, (0,0,255), (640, 480), (x, y))
		pygame.display.update()