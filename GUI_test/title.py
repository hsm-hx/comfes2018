# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():
  pygame.init()
  screen = pygame.display.set_mode((1280, 720), 0, 32)
  pygame.display.set_caption("リリアと虹色の夜想曲")
  #bg = pygame.image.load("img/bg.jpg").convert_alpha()
  #rect_bg = bg.get_rect()
  font = pygame.font.Font("GenShinGothic-Medium.ttf", 55)

  menu_pointer = 0

  while(1):
    menu_start = font.render("START", True, (255, 255, 255))
    menu_quit = font.render("QUIT", True, (255, 255, 255))
    caption = font.render("上下キーで選択・スペースキーで決定", True, (255, 255, 255))

    arrow = font.render("->", True, (255,255,255))

    screen.fill((0,20,0, 0))
    #screen.blit(bg, rect_bg)
    screen.blit(menu_start, [100, 100])
    screen.blit(menu_quit, [100, 200])
    screen.blit(caption, [200, 500])

    if menu_pointer == 0:
      screen.blit(arrow, [50, 100])
    elif menu_pointer == 1:
      screen.blit(arrow, [50, 200])

    pygame.display.update()

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()
        if event.key == K_DOWN or event.key == K_UP:
          if menu_pointer == 1:
            menu_pointer = 0
          else:
            menu_pointer = 1
        if event.key == K_SPACE:
          if menu_pointer == 0:
            continue
          elif menu_pointer == 1:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
  main()
  
