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

def main():
  hand_player = 5*[0]
  hand_enemy = 5*[0]
  c_back = pygame.image.load("../img/card_back.png").convert_alpha()
  c_back = pygame.transform.scale(c_back, (int(136 * 0.75), int(200 * 0.75)))
  my_icon = pygame.image.load("../img/lilia_icon.png").convert_alpha()
  my_status = pygame.image.load("../img/player_status.png").convert_alpha()
  enemy_icon = pygame.image.load("../img/lilia_icon.png").convert_alpha()
  enemy_status = pygame.transform.flip(my_status, True, True)
  text_frame = pygame.image.load("../img/frame.png").convert_alpha()
  bg = pygame.image.load("../img/bg.jpg").convert_alpha()
  bg = pygame.transform.scale(bg, (1280, 720))
  bg_mask = pygame.image.load("../img/bg-mask.png").convert_alpha()

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
      screen.blit(my_icon, (-50, 520))
      screen.blit(enemy_status, (730, 5))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)
        screen.blit(c_back, (i*110, 0))

      screen.blit(bg_mask, (0,0))
      screen.blit(text_frame, (40,100))

      text = ["よし、それじゃあゲームの説明をしよう。準備はいいか？","まずはこの街、”キノ”で最も一般的なゲーム…\nポーカーについて教えてやる。"]
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
      screen.blit(my_icon, (-50, 520))
      screen.blit(enemy_status, (730, 5))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(5):
        screen.blit(c_back, (i*110, 0))

      screen.blit(bg_mask, (0,0))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)

      screen.blit(text_frame, (40,500))

      text = ["ここにあるのが嬢ちゃんの手札だ。\nワンセットのトランプの中から、ランダムに5枚が配られる。","おっと、わかっちゃいるだろうが勿論イカサマは無しだぜ？"]
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
      screen.blit(enemy_status, (730, 5))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)
        screen.blit(c_back, (i*110, 0))

      screen.blit(bg_mask, (0,0))

      screen.blit(my_icon, (-50, 520))  
      screen.blit(text_frame, (40,100))

      text = ["これは嬢ちゃんの”運”が可視化されたもの。\nこいつが多く溜まってるほど良い役が揃いやすくなる。"]
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
      screen.blit(my_icon, (-50, 520))  
      screen.blit(enemy_status, (730, 5))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)
        screen.blit(c_back, (i*110, 0))

      screen.blit(bg_mask, (0,0))

      screen.blit(my_status, (160, 590))
      screen.blit(text_frame, (40,100))

      text = ["ここには継続中のアビリティ効果、\n下段には現在の所持金が表示される。", "賭けの世界じゃ金が全てだ。所持金はしっかり確認するようにな！"]
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
      screen.blit(my_icon, (-50, 520))  
      screen.blit(enemy_status, (730, 5))
      screen.blit(enemy_icon, (1100, -50))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)

      screen.blit(bg_mask, (0,0))

      for i in range(5):
        screen.blit(c_back, (i*110, 0))
      screen.blit(text_frame, (40,500))

      text = ["こいつは対戦相手の手札だ。\n特別なアビリティを使わない限りは嬢ちゃんからは見えないぜ。"]
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
      screen.blit(my_icon, (-50, 520))  
      screen.blit(enemy_status, (730, 5))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)
        screen.blit(c_back, (i*110, 0))

      screen.blit(bg_mask, (0,0))

      screen.blit(enemy_icon, (1100, -50))
      screen.blit(text_frame, (40,500))

      text = ["これが対戦相手の運ゲージ、"]
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
      screen.blit(my_icon, (-50, 520))  
      screen.blit(enemy_icon, (1100, -50))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)
        screen.blit(c_back, (i*110, 0))

      screen.blit(bg_mask, (0,0))

      screen.blit(enemy_status, (730, 5))
      screen.blit(text_frame, (40,500))

      text = ["そしてこれは対戦相手に継続中のアビリティ効果だ。"]
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
      screen.blit(my_icon, (-50, 520))  
      screen.blit(enemy_icon, (1100, -50))

      for i in range(len(hand_player)):
        hand_player[i].show(i*170 + 400, 250)
        screen.blit(c_back, (i*110, 0))

      screen.blit(bg_mask, (0,0))

      screen.blit(enemy_status, (730, 5))
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

      if line_count == len(text): break

if __name__ == '__main__':
  main()