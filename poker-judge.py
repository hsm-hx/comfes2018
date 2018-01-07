def straight_flush(hand):
  if flush(hand) and straight(hand):
    return True
  else:
    return False

def flush(hand):
  suit = hand[0]

  for i in hand:
    if hand[i].suit == suit:
      continue
    else:
      return False

  return True

def one_pair(hand):
  for i in hand:
    for j in hand:
      if j <= i:
        continue
      else:
        if j.rank == i.rank:
          return True

  return False

def judgement(hand):
  #if straight_flush(hand) == True:
  #  return "Straight Flush"
  #four_of_a_kind(hand)
  #full_house(hand)
  #flush(hand)
  #straight(hand)
  #three_of_a_kind(hand)
  #two_pair(hand)
  one_pair(hand)

  else:
    return "High Cards"