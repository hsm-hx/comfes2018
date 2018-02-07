import random
from operator import attrgetter
import pygame
from pygame.locals import *
import sys
import judge
import ability
import hands

SUIT = 4
RANK = 13

(w, h) = (1280, 720)
pygame.init()
pygame.display.set_mode((w, h), 0, 32)
screen = pygame.display.get_surface()
font = pygame.font.Font("font/GenShinGothic-Medium.ttf", 55)

def main():
  hand = sorted(hands.redraw(), key=attrgetter('rank'))

  result = font.render(judge.judgement(hand), True, (255,255,255))
  screen.blit(result, (500,400))
  pygame.display.update()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()

if __name__ == '__main__':
  main()