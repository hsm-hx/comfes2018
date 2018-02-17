# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import story

def main():
  count_part = 1
  while True:
    if story.story(str(count_part)) == True:
      count_part += 1

if __name__ == '__main__':
  main()