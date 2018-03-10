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
font = pygame.font.Font("fonts/cinecap.ttf", 30)
font_UI = pygame.font.Font("fonts/Gen-Medium.ttf", 20)
CLOCK = pygame.time.Clock()

def main():
  hand_player = 5*[0]
  hand_enemy = 5*[0]
  my_hp_cur = 200
  my_hp_max = 200
  my_mp_cur = 100
  my_mp_max = 100
  enemy_hp_cur = 100
  enemy_hp_max = 100
  enemy_mp_cur = 50
  enemy_mp_max = 50
  c_back = pygame.image.load("../img/card_back.png").convert_alpha()
  c_back_sml = pygame.transform.scale(c_back, (int(136 * 0.75), int(200 * 0.75)))
  my_icon = pygame.image.load("../img/lilia_icon.png").convert_alpha()
  my_status = pygame.image.load("../img/player_status.png").convert_alpha()
  enemy_icon = pygame.image.load("../img/lilia_icon.png").convert_alpha()
  enemy_status = pygame.transform.flip(my_status, True, True)
  text_frame = pygame.image.load("../img/frame.png").convert_alpha()
  bg = pygame.image.load("../img/bg.jpg").convert()
  bg = pygame.transform.scale(bg, (1280, 720))
  bg_mask = pygame.image.load("../img/bg-mask.png").convert()
  bg_mask.set_alpha(192)
  hp = font.render("HP", True, (0,0,0))
  mp = font.render("MP", True, (0,0,0))

  hand_player[0] = hands.Card(1,10)
  hand_player[1] = hands.Card(4, 7)
  hand_player[2] = hands.Card(4, 8)
  hand_player[3] = hands.Card(3, 1)
  hand_player[4] = hands.Card(2,10)

  hand_enemy[0] = hands.Card(4, 9)
  hand_enemy[1] = hands.Card(2, 6)
  hand_enemy[2] = hands.Card(3, 8)
  hand_enemy[3] = hands.Card(1, 9)
  hand_enemy[4] = hands.Card(4, 10)

  while True:
    line_count = 0
    while True:
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(enemy_icon, (1100, -50))


      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)
        screen.blit(c_back_sml, (i*110, 0))

      screen.blit(bg_mask, (0,0))
      screen.blit(text_frame, (40,100))

      text = ["よし、それじゃあゲームの説明をしよう。準備はいいか？","まずはこの街、”キノ”で最も一般的なゲーム…\nポーカーについて教えてやる。"]
      if '\n' in text[line_count]:
        line = text[line_count].split('\n')
        sur_text = [font.render(line[0], True, (0,0,0)),
                    font.render(line[1], True, (0,0,0))]
        screen.blit(sur_text[0], (100, 120))
        screen.blit(sur_text[1], (100, 160))
      else:
        sur_text = font.render(text[line_count], True, (0,0,0))
        screen.blit(sur_text, (100,120))

      pygame.display.update()

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE: 
            pygame.quit()
            sys.exit()
          if event.key == K_RETURN:
            line_count += 1

      if line_count == len(text): break

    line_count = 0
    while True:
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(5):
        screen.blit(c_back_sml, (i*110, 0))

      screen.blit(bg_mask, (0,0))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)

      screen.blit(text_frame, (40,500))

      text = ["ここにあるのが嬢ちゃんの手札だ。\nワンセットのトランプの中から、ランダムに5枚が配られる。","おっと、わかっちゃいるだろうが勿論イカサマは無しだぜ？"]

      if '\n' in text[line_count]:
        line = text[line_count].split('\n')
        sur_text = [font.render(line[0], True, (0,0,0)),
                    font.render(line[1], True, (0,0,0))]
        screen.blit(sur_text[0], (100, 520))
        screen.blit(sur_text[1], (100, 560))
      else:
        sur_text = font.render(text[line_count], True, (0,0,0))
        screen.blit(sur_text, (100,520))

      pygame.display.update()

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE: 
            pygame.quit()
            sys.exit()
          if event.key == K_RETURN:
            line_count += 1

      if line_count == len(text): break

    line_count = 0
    while True:
      screen.blit(bg, (0,0))
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)
        screen.blit(c_back_sml, (i*110, 0))

      screen.blit(bg_mask, (0,0))

      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))  
      screen.blit(text_frame, (40,100))

      text = ["これは嬢ちゃんに残っているHP(体力)、MP(精神力)を表している。\nHPが尽きると嬢ちゃんの負けってことだ。",
              "賭けってのは結構な気力を使う。”アビリティ”なんかを使うと特にな。\nこの２つはしっかり確認するんだぞ。"]

      if '\n' in text[line_count]:
        line = text[line_count].split('\n')
        sur_text = [font.render(line[0], True, (0,0,0)),
                    font.render(line[1], True, (0,0,0))]
        screen.blit(sur_text[0], (100, 120))
        screen.blit(sur_text[1], (100, 160))
      else:
        sur_text = font.render(text[line_count], True, (0,0,0))
        screen.blit(sur_text, (100,120))

      pygame.display.update()

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE: 
            pygame.quit()
            sys.exit()
          if event.key == K_RETURN:
            line_count += 1

      if line_count == len(text): break

    line_count = 0
    while True:
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))  
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)

      screen.blit(bg_mask, (0,0))

      for i in range(5):
        screen.blit(c_back_sml, (i*110, 0))
      screen.blit(text_frame, (40,500))

      text = ["こいつは対戦相手の手札だ。\n特別なアビリティを使わない限りは嬢ちゃんからは見えないぜ。"]

      if '\n' in text[line_count]:
        line = text[line_count].split('\n')
        sur_text = [font.render(line[0], True, (0,0,0)),
                    font.render(line[1], True, (0,0,0))]
        screen.blit(sur_text[0], (100, 520))
        screen.blit(sur_text[1], (100, 560))
      else:
        sur_text = font.render(text[line_count], True, (0,0,0))
        screen.blit(sur_text, (100,520))

      pygame.display.update()

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE: 
            pygame.quit()
            sys.exit()
          if event.key == K_RETURN:
            line_count += 1

      if line_count == len(text): break

    line_count = 0
    while True:
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))  
      screen.blit(enemy_icon, (1100, -50))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)
        screen.blit(c_back_sml, (i*110, 0))

      screen.blit(bg_mask, (0,0))

      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(text_frame, (40,500))

      text = ["そしてこれは対戦相手のHP/MPを表している。"]
      sur_text = font.render(text[line_count], True, (0,0,0))
      screen.blit(sur_text, (100,520))

      pygame.display.update()

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE: 
            pygame.quit()
            sys.exit()
          if event.key == K_RETURN:
            line_count += 1

      if line_count == len(text): break

    line_count = 0
    while True:
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))  
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)
        screen.blit(c_back_sml, (i*110, 0))

      screen.blit(bg_mask, (0,0))

      screen.blit(text_frame, (40,100))

      text = ["ここまでは大丈夫だな？それじゃ、ポーカーの遊び方を説明していくぜ。"]
      sur_text = font.render(text[line_count], True, (0,0,0))
      screen.blit(sur_text, (100,120))

      pygame.display.update()

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE: 
            pygame.quit()
            sys.exit()
          if event.key == K_RETURN:
            line_count += 1

      if line_count == len(text): 
        i = 192
        break

    while i <= 255:
      bg_mask.set_alpha(i)
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520)) 
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70)) 
      screen.blit(enemy_icon, (1100, -50))
      for j in range(len(hand_player)):
        hand_player[j].show(j*170 + 400, 250)
        screen.blit(c_back_sml, (j*110, 0))
      screen.blit(text_frame, (40,100))
      sur_text = font.render(text[len(text)-1], True, (0,0,0))
      screen.blit(sur_text, (100,120))
      screen.blit(bg_mask, (0,0))
      pygame.display.update()          
      i += 1
      CLOCK.tick(30)

    for i in range(60):
      CLOCK.tick(30)

    i = 255

    while i > 192:
      bg_mask.set_alpha(i)
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))  
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(enemy_icon, (1100, -50))

      screen.blit(bg_mask, (0,0))
      pygame.display.update()          
      i -= 1
      CLOCK.tick(30)
      

    line_count = 0
    while True:
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))  
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(enemy_icon, (1100, -50))

      screen.blit(bg_mask, (0,0))
      screen.blit(text_frame, (40,100))

      text = ["さて、練習試合の幕開けだ。しっかりゲームの流れを頭に入れるんだぞ？"]
      sur_text = font.render(text[line_count], True, (0,0,0))
      screen.blit(sur_text, (100,120))

      pygame.display.update()

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE: 
            pygame.quit()
            sys.exit()
          if event.key == K_RETURN:
            line_count += 1

      if line_count == len(text): break

    hand_player = [hands.Card(2,13), hands.Card(1,3), hands.Card(1,8), hands.Card(3,11), hands.Card(3,13)]

    while True:
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(len(hand_player)):
        count = -200
        while count <= 250:
          screen.blit(bg, (0,0))
          screen.blit(my_status, (160, 590))
          my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
          my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
          screen.blit(hp, (180, 595))
          my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
          screen.blit(my_hp_line, (405, 610))
          screen.blit(mp, (180, 640))
          my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
          screen.blit(my_mp_line, (405, 655))
          screen.blit(my_icon, (-50, 520))
          screen.blit(enemy_status, (730, 5))
          enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
          enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
          screen.blit(hp, (1070, 10))
          enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
          screen.blit(enemy_hp_line, (760, 25))
          screen.blit(mp, (1070, 55))
          enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
          screen.blit(enemy_mp_line, (790, 70)) 
          screen.blit(enemy_icon, (1100, -50))
          for j in range(i):
            screen.blit(c_back, (j*170 + 400, 250))
          for j in range(5):
            screen.blit(c_back_sml, (j*110, 0))
          screen.blit(c_back, (i*170 + 400, count))
          pygame.display.update()
          count += 50
          CLOCK.tick(30)

      break

    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, (255,255,255), Rect(780, 580, 500, 120))
    screen.blit(my_status, (160, 590))
    my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
    my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
    screen.blit(hp, (180, 595))
    my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
    screen.blit(my_hp_line, (405, 610))
    screen.blit(mp, (180, 640))
    my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
    screen.blit(my_mp_line, (405, 655))
    screen.blit(my_icon, (-50, 520))
    screen.blit(enemy_status, (730, 5))
    enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
    enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
    screen.blit(hp, (1070, 10))
    enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
    screen.blit(enemy_hp_line, (760, 25))
    screen.blit(mp, (1070, 55))
    enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
    screen.blit(enemy_mp_line, (790, 70))
    screen.blit(enemy_icon, (1100, -50))

    for i in range(len(hand_player)):
      hand_player[i].show(i*170 + 400, 250)
      screen.blit(c_back_sml, (i*110, 0))

    pygame.display.update()
      
    for i in range(50):
      CLOCK.tick(30)

    line_count = 0
    while True:
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(5):
        screen.blit(c_back_sml, (i*110, 0))

      screen.blit(bg_mask, (0,0))
      screen.blit(text_frame, (40,500))
      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)

      text = ["今、ここに手札が配られたのがわかるな？\nこの手札は1度だけ交換ができる。",
              "手札の中に、同じ絵の種類…スートが揃っていたり、\n同じ数字、連番の数字が揃っている組み合わせを役という。",
              "役の種類はたくさんある。\n一覧にしたものがこれだ。",
              "まあ初めのうちはなかなか覚えられんだろうが、そのうち慣れる。\n俺たちもそうしてきたからな。",
              "それじゃあ、まずは真ん中の3枚を交換してみることにしよう。\n十字キーの左右でカードを選択、エンターキーで確定だ。"]

      if '\n' in text[line_count]:
        line = text[line_count].split('\n')
        sur_text = [font.render(line[0], True, (0,0,0)),
                    font.render(line[1], True, (0,0,0))]
        screen.blit(sur_text[0], (100, 520))
        screen.blit(sur_text[1], (100, 560))
      else:
        sur_text = font.render(text[line_count], True, (0,0,0))
        screen.blit(sur_text, (100,520))

      pygame.display.update()

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE: 
            pygame.quit()
            sys.exit()
          if event.key == K_RETURN:
            line_count += 1
      
      if line_count == len(text):
        break      

    line_count = 0
    change = 5*[False]
    key_pointer = 0
    cursor = font.render("▲", True, (255,255,255))

    while True:
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(5):
        screen.blit(c_back_sml, (i*110, 0))

      screen.blit(bg_mask, (0,0))
      screen.blit(text_frame, (40,500))
      for i in range(len(hand_player)):
        if change[i] == True:
          hand_player[i].show(i*170 + 400, 200)
        else:
          hand_player[i].show(i*170 + 400, 250)

      if key_pointer == 5:
        key_pointer = 0
      if key_pointer == -1:
        key_pointer = 4

      text = ["それじゃあ、まずは真ん中の3枚を交換してみることにしよう。\n十字キーの左右でカードを選択、エンターキーで確定だ。"]

      if '\n' in text[line_count]:
        line = text[line_count].split('\n')
        sur_text = [font.render(line[0], True, (0,0,0)),
                    font.render(line[1], True, (0,0,0))]
        screen.blit(sur_text[0], (100, 520))
        screen.blit(sur_text[1], (100, 560))
      else:
        sur_text = font.render(text[line_count], True, (0,0,0))
        screen.blit(sur_text, (100,520))

      screen.blit(cursor, [key_pointer*200+400, 450])

      pygame.display.update()
      
      if change[1] == True and change[2] == True and change[3] == True:
        for i in range(30):
          CLOCK.tick(30)
        break

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE: 
            pygame.quit()
            sys.exit()
          if event.key == K_RETURN:
            change[key_pointer] = True
          if event.key == K_LEFT:
            key_pointer -= 1
          if event.key == K_RIGHT:
            key_pointer += 1

    while True:
      screen.blit(bg, (0,0))
      screen.blit(my_status, (160, 590))
      my_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 630, 250, 10))
      my_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(150, 675, 250, 10))
      screen.blit(hp, (180, 595))
      my_hp_line = font.render(str(my_hp_cur)+'/'+str(my_hp_max), True, (0,0,0))
      screen.blit(my_hp_line, (405, 610))
      screen.blit(mp, (180, 640))
      my_mp_line = font.render(str(my_mp_cur)+'/'+str(my_mp_max), True, (0,0,0))
      screen.blit(my_mp_line, (405, 655))
      screen.blit(my_icon, (-50, 520))
      screen.blit(enemy_status, (730, 5))
      enemy_hp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 45, 250, 10))
      enemy_mp = pygame.draw.rect(screen, (255, 64, 64), Rect(870, 90, 250, 10))
      screen.blit(hp, (1070, 10))
      enemy_hp_line = font.render(str(enemy_hp_cur)+'/'+str(enemy_hp_max), True, (0,0,0))
      screen.blit(enemy_hp_line, (760, 25))
      screen.blit(mp, (1070, 55))
      enemy_mp_line = font.render(str(enemy_mp_cur)+'/'+str(enemy_mp_max), True, (0,0,0))
      screen.blit(enemy_mp_line, (790, 70))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(5):
        screen.blit(c_back_sml, (i*110, 0))

      screen.blit(bg_mask, (0,0))
      screen.blit(text_frame, (40,500))
      for i in range(len(hand_player)):
        if change[i] == True:
          hand_player[i].show(i*170 + 400, 200)
        else:
          hand_player[i].show(i*170 + 400, 250)

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