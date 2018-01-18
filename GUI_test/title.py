# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():
  pygame.init()
  screen = pygame.display.set_mode((1280, 720), 0, 32)
  pygame.display.set_caption("リリアと虹色の夜想曲")
  bg = pygame.image.load("img/bg.jpg").convert_alpha()
  rect_bg = bg.get_rect()
  font = pygame.font.Font(None, 55)

  while(1):
    menu_start = font.render("START", True, (255, 255, 255))
    menu_quit = font.render("QUIT", True, (255, 255, 255))

    screen.fill((0,20,0, 0))
    screen.blit(bg, rect_bg)
    screen.blit(menu_start, [100, 200])
    screen.blit(menu_quit, [100, 100])

    pygame.display.update()

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()

if __name__ == "__main__":
  main()
  
