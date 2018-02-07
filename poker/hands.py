import random
import pygame
from pygame.locals import *
import sys
import ability

SUIT = 4
RANK = 13

(w, h) = (1280, 720)
pygame.init()
pygame.display.set_mode((w, h), 0, 32)
screen = pygame.display.get_surface()
font = pygame.font.Font("font/GenShinGothic-Medium.ttf", 55)
cursor = font.render("▼", True, (255,255,255))

class Card():
  def __init__(self, suit, rank):
    if suit==0: self.suit="heart"
    elif suit==1: self.suit="diamond"
    elif suit==2: self.suit="spade"
    else: self.suit="club"

    self.rank=rank

    if self.rank < 10:
      img_path = "img/card_" + self.suit + "_0" + str(self.rank) + ".png"
    else:
      img_path = "img/card_" + self.suit + "_" + str(self.rank) + ".png"
    self.img = pygame.image.load(img_path).convert_alpha()
    
  def show(self, pos_x, pos_y):
    screen.blit(self.img, (pos_x, pos_y)) 

def deck_init(deck):
  count = 0

  for i in range(SUIT):
    for j in range(RANK):
      deck[count] = Card(i, j+1)
      count += 1

def hand_init(hand):
  for i in hand:
    hand = Card(0,1)

def hand_draw(index, hand, deck):
  hand[index] = deck[random.randint(0, 52-1)]
  for i in range(len(hand)):
    if i != index:
      while hand[i]==hand[index]:
        hand[index] = deck[random.randint(0, 52-1)]

def redraw():
  deck = 52*[0] # Initialize by 0
  hand = 5*[0] # initialize by 0
  change = 5*[False]
  count = 0
  key_pointer = 0
  
  deck_init(deck)
  hand_init(hand)
  for i in range(len(hand)):
    hand_draw(i, hand, deck)

  for i in range(len(hand)):
    hand[i].show(i*200, 500)

  pygame.display.update() 

  while True:
    screen.fill((0, 0, 0, 0))
    
    for i in range(len(hand)):
      hand[i].show(i*200, 500)
          
    if key_pointer == 5:
      key_pointer -= 5
    if key_pointer == -1:
      key_pointer += 5
    
    for i in change:
      if i == True:
        screen.blit(cursor, [count*200, 300])
      count += 1
    screen.blit(cursor, [key_pointer*200, 0])
    pygame.display.update()
    count = 0
  
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE: 
          pygame.quit()
          sys.exit()
        if event.key == K_LEFT:
          key_pointer -= 1
        if event.key == K_RIGHT:
          key_pointer += 1
        if event.key == K_SPACE:
          if change[key_pointer] == False:
            change[key_pointer] = True
          else:
            change[key_pointer] = False
        if event.key == K_RETURN:
          for i in change:
            if i == False:
              break
            else:
              hand_draw(count, hand, deck)
            count += 1
          screen.fill((0,0,0,0))
          for i in range(len(hand)):
            hand[i].show(i*200, 500)
          return hand

          screen.fill((0,0,0,0))
          for i in range(len(hand)):
            hand[i].show(i*200, 500)
          screen.blit(cursor, [key_pointer*200, 0])
          pygame.display.update()
          count = 0
