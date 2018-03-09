# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys

class Script:
  def __init__(self, name, line):
    self.name = name
    self.line = line

def story(part):
  pygame.init()
  screen = pygame.display.set_mode((1280,720))
  pygame.display.set_caption("リリアと虹色の夜想曲")
  font = pygame.font.Font("font/cinecap.ttf", 30)
  text_frame = pygame.image.load("img/frame.png").convert_alpha()
  bg = pygame.image.load("img/1/town.jpg").convert_alpha()
  lilia_stand = pygame.image.load("img/girl.png").convert_alpha()
  man_stand = pygame.image.load("img/man.png").convert_alpha()
  rect_bg = bg.get_rect()
  rect_tf = text_frame.get_rect()
  rect_tf.center = (480,600)
  rect_lilia_stand = lilia_stand.get_rect()
  rect_man_stand = man_stand.get_rect()
  script = []

  fpass = "script/" + part + ".txt"
  
  name = None
  line = None

  for l in open(fpass, 'r'):
    if l.find('name:') != -1:
      name = l[5:].rstrip()
    if l.find('line:') != -1:
      line = l[5:].rstrip()

    if name is not None and line is not None:
      script.append(Script(name, line))
      name = None
      line = None

  script[0].name = script[0].name.lstrip(':')
  line_count = 0

  while(1):
    try:
      check_in_range = script[line_count].name
    except IndexError:
      return True
    else:
      cur_name = font.render(script[line_count].name, True, (0,0,0))
      cur_line = font.render(script[line_count].line, True, (0,0,0))
      screen.fill((0,0,0))
      screen.blit(bg, rect_bg)
      screen.blit(lilia_stand, [200, 200])
      screen.blit(man_stand, [600, 200])
      screen.blit(text_frame, rect_tf)
      screen.blit(cur_name, [20, 490])
      screen.blit(cur_line, [20, 550])
      pygame.display.update()
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
          if event.key == K_SPACE:
            line_count += 1
