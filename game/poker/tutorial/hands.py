import random
import pygame
from pygame.locals import *
import sys

SUIT = 4
RANK = 13

(w, h) = (1280, 720)
pygame.init()
pygame.display.set_mode((w, h), 0, 32)

screen = pygame.display.get_surface()
font = pygame.font.Font("fonts/cinecap.ttf", 55)
cursor = font.render("▼", True, (255,255,255))

class Card():
  def __init__(self, suit, rank):
    if suit==0: self.suit="heart"
    elif suit==1: self.suit="diamond"
    elif suit==2: self.suit="spade"
    else: self.suit="club"

    self.rank=rank

    if self.rank < 10:
      img_path = "../img/card_" + self.suit + "_0" + str(self.rank) + ".png"
    else:
      img_path = "../img/card_" + self.suit + "_" + str(self.rank) + ".png"
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
    i = Card(0,1)

def hand_draw(index, hand, deck):
  hand[index] = deck[random.randint(0, 52-1)]
  for i in range(len(hand)):
    if i != index:
      while hand[i]==hand[index]:
        hand[index] = deck[random.randint(0, 52-1)]

def redraw():
  deck = 52*[0] # Initialize by 0
  hand_player = 5*[0] # initialize by 0
  change_player = 5*[False]
  hand_enemy = 5*[0]
  change_enemy = 5*[False]
  count = 0
  key_pointer = 0
  
  deck_init(deck)
  hand_init(hand_player)
  hand_init(hand_enemy)
  for i in range(len(hand_player)):
    hand_draw(i, hand_player, deck)
  for i in range(len(hand_enemy)):
    hand_draw(i, hand_enemy, deck)

  for i in range(len(hand_player)):
    hand_player[i].show(i*200, 500)
  for i in range(len(hand_enemy)):
    hand_enemy[i].show(i*200, 100)

  pygame.display.update() 

  while True:
    screen.fill((0, 0, 0, 0))
    
    for i in range(len(hand_player)):
      hand_player[i].show(i*200, 500)
    for i in range(len(hand_enemy)):
      hand_enemy[i].show(i*200, 100)
          
    if key_pointer == 5:
      key_pointer -= 5
    if key_pointer == -1:
      key_pointer += 5
    
    for i in change_player:
      if i == True:
        screen.blit(cursor, [count*200, 400])
      count += 1
    screen.blit(cursor, [key_pointer*200, 350])
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
          if change_player[key_pointer] == False:
            change_player[key_pointer] = True
          else:
            change_player[key_pointer] = False
        if event.key == K_RETURN:
          for i in change_player:
            if i == False:
              break
            else:
              hand_draw(count, hand_player, deck)
            count += 1
          screen.fill((0,0,0,0))
          for i in range(len(hand_player)):
            hand_player[i].show(i*200, 500)
          return hand_player

          screen.fill((0,0,0,0))
          for i in range(len(hand_player)):
            hand_player[i].show(i*200, 500)
          screen.blit(cursor, [key_pointer*200, 0])
          pygame.display.update()
          count = 0
