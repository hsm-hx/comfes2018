import pygame
from pygame.locals import *
import sys
import hands

SUIT = 4
RANK = 13

(w, h) = (1280, 720)
pygame.init()
pygame.display.set_mode((w, h), 0, 32)
screen = pygame.display.get_surface()
font = pygame.font.Font("fonts/cinecap.ttf", 55)

def main():
  hand = 5*[0]
  hands.hand_init(hand)

  hand[0] = hands.Card(1,10)
  hand[1] = hands.Card(4, 7)
  hand[2] = hands.Card(4, 8)
  hand[3] = hands.Card(3, 1)
  hand[4] = hands.Card(2,10)

  while True:
    for i in range(len(hand)):
      hand[i].show(i*170 + 400, 250)

    pygame.display.update()

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