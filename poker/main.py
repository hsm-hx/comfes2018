import pygame
import poker

(w,h) = (1280, 720)

pygame.init()
pygame.display.set_mode((w,h), 0, 32)
screen = pygame.display.get_surface()

poker.main()
