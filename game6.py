#create my name font image
my_name = "Gin Lee"
import pygame
pygame.init()
my_font = pygame.font.SysFont("arial", 64)
name_surface = my_font.render(my_name, True, (0,255,0))
pygame.image.save(name_surface, "name.jpg")
