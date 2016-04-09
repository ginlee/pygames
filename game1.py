#!usr/bin/env python

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

import pygame
#import pygame frame
from pygame.locals import *
#import some useful functions from pygame
from sys import exit
#borrow an exit function from sys frame
pygame.init()
#initial pygame, prepare for some hardware device
screen = pygame.display.set_mode((640,480), 0, 32)

pygame.display.set_caption('Hello, World!')

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert()

while True:
#main loop for our game
    for event in pygame.event.get():
        if event.type == QUIT:
            #quit the game
            exit()
    screen.blit(background, (0,0))
    x, y = pygame.mouse.get_pos()
    x-=mouse_cursor.get_width()/2
    y-=mouse_cursor.get_height()/2
    #calculate the mouse left above corne position
    screen.blit(mouse_cursor,(x,y))

    pygame.display.update()
