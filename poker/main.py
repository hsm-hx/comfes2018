import random
from operator import attrgetter
import judge
import ability

SUIT = 4
RANK = 13

class Card():
  def __init__(self, suit, rank):
    if suit==0: self.suit="Heart"
    elif suit==1: self.suit="Dia"
    elif suit==2: self.suit="Spade"
    else: self.suit="Club"

    self.rank=rank

  def show(self):
    print(self.suit+'-', end='')

    if self.rank == 1: print('A')
    elif self.rank == 11: print('J')
    elif self.rank == 12: print('Q')
    elif self.rank == 13: print('K')
    else: print(self.rank)


def deck_init(deck):
  count = 0

  for i in range(SUIT):
    for j in range(RANK):
      deck[count] = Card(i, j+1)
      count += 1

def hand_init(hand):
  for i in hand: hand = Card(0,0)

def hand_draw(index, hand, deck):
  hand[index] = deck[random.randint(0, 52-1)]
  for i in range(len(hand)):
    if i != index:
      while hand[i]==hand[index]:
        hand[index] = deck[random.randint(0, 52-1)]


if __name__ == '__main__':
  deck = 52*[0] # Initialize by 0
  hand = 5*[0] # initialize by 0
  change = 5*[9]
  count = 0
  deck_init(deck)
  hand_init(hand)
  for i in range(len(hand)):
    hand_draw(i, hand, deck)

  for i in range(len(hand)):
    print(str(i+1) + " : ", end="")
    hand[i].show()

  #Change hands
  print("Input numbers you want to change")
  print("If you finish choosing, press F")

  while True:
    ch = input()

    #When F inputted, finish change phase
    if ch == 'F': break

    #I must rewrite this code to be inputed Alphabet which is not 'F'
    elif 1<=int(ch) and int(ch)<=5:
      change[count] = int(ch)-1
      count += 1

    else: continue

  print("Change Cards: ", end="")
  for i in change:
    if i == 9:
      break
    else:
      print(str(i+1) + ' ', end="")
      hand_draw(i, hand, deck)

  print("\nChange Result")
  for i in range(len(hand)):
    print(str(i+1) + " : ", end="")
    hand[i].show()

  #sort by rank
  hand = sorted(hand, key=attrgetter('rank'))

  print(judge.judgement(hand))
  