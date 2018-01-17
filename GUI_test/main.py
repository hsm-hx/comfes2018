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

  while(1):
    pygame.display.update()
    pygame.time.wait(30)
    screen.fill((0,20,0, 0))
    screen.blit(bg, rect_bg)

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
  
