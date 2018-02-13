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

def full_house(hand):
  if hand[0].rank == hand[1].rank:
    if hand[2].rank == hand[3].rank == hand[4].rank:
      return True
  elif hand[0].rank == hand[1].rank == hand[2].rank:
    if hand[3].rank == hand[4].rank:
      return True
  return False

def four_of_a_kind(hand):
  if hand[0].rank == hand[1].rank == hand[2].rank == hand[3].rank:
    return True
  elif hand[1].rank == hand[2].rank == hand[3].rank == hand[4].rank:
    return True
  else:
    return False

def three_of_a_kind(hand):
  if hand[0].rank == hand[1].rank == hand[2].rank:
    return True
  elif hand[1].rank == hand[2].rank == hand[3].rank:
    return True
  elif hand[2].rank == hand[3].rank == hand[4].rank:
    return True
  else:
    return False

def two_pair(hand):
  pair_rank = one_pair(hand)

  if pair_rank is not None:
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
  elif full_house(hand) == True:
    return "Full House"
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