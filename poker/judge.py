def straight_flush(hand):
  if flush(hand) and straight(hand):
    return True
  else:
    return False

def flush(hand):
  suit = hand[0].suit

  for i in hand:
    if hand[hand.index(i)].suit == suit:
      continue
    else:
      return False
  return True

def straight(hand):
  for i in hand:
    if i.rank == hand[hand.index(i)+1].rank+1:
      continue
    else:
      return False
  #10-J-Q-K-A 
  return True

def four_of_a_kind(hand):
  for i in range(len(hand)):
    if hand[i].rank != hand[i+1].rank and hand[i+1].rank != hand[i+2].rank:
      return False
    elif hand[i].rank == hand[i+1].rank:
      for j in hand:
        if hand[i].rank == j.rank:
          continue
        else:
          return False
    else:
      for j in hand:
        if hand.index(j) == 0:
          continue
        elif j.rank == hand[1].rank:
          continue
        else:
          return False
  return True

def three_of_a_kind(hand):
  if hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank:
    return True
  elif hand[1].rank == hand[2].rank and hand[2].rank == hand[3].rank:
    return True
  elif hand[2].rank == hand[3].rank and hand[3].rank == hand[4].rank:
    return True
  else:
    return False

def two_pair(hand):
  pair_rank = one_pair(hand)

  if pair_rank != NULL:
    for i in hand:
      for j in hand:
        if hand.index(j) <= hand.index(i):
          continue
        else:
          if j.rank == i.rank and j.rank != pair_rank:
            return True
  return False

def one_pair(hand):
  for i in hand:
    for j in hand:
      if hand.index(j) <= hand.index(i):
        continue
      else:
        if j.rank == i.rank:
          return j.rank
  return None

def judgement(hand):
  if straight_flush(hand) == True:
    return "Straight Flush"
  elif four_of_a_kind(hand) == True:
    return "Four of a Kind"
  #full_house(hand)
  elif flush(hand) == True:
    return "Flush"
  elif straight(hand) == True:
    return "Straight"
  elif three_of_a_kind(hand) == True:
    return "Three of a Kind"
  elif two_pair(hand) == True:
    return "Two Pair"
  elif one_pair(hand) is not None:
    return "One Pair"

  else:
    return "High Cards"