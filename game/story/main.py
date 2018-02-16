# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys

class Script:
  def __init__(self, name, line):
    self.name = name
    self.line = line

def main(part):
  pygame.init()
  screen = pygame.display.set_mode((1280,720))
  pygame.display.set_caption("リリアと虹色の夜想曲")
  font = pygame.font.Font("font/Gen-Medium.ttf", 55)
  script = []

  fpass = "script/" + part + ".txt"
  
  name = None
  line = None

  for l in open(fpass, 'r'):
    if l.find('name:') != -1:
      name = l[5:]
    if l.find('line:') != -1:
      line = l[5:]

    if name is not None and line is not None:
      script.append(Script(name, line))
      name = None
      line = None

  """
  program to debug

  for i in script:
    print(i.name)
    print(i.line)
  """

  while(1):
    screen.fill((0,0,0))
    text = font.render("TEST", True, (255,255,255))
    screen.blit(text, [20,100])
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
  main("1")