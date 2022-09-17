import random
#import logo from art
#import clear from replit
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def dealcard():
    return random.choice(cards)


def calculate_score(playercards):
  score = sum(playercards)
  if score == 21:
    return 0
  else:
    if score > 21:
      for card in playercards:
        if card == 11:
          playercards.remove(11)
          playercards.append(1)
          score = sum(playercards)
    return score


user_cards = []
comp_cards = []
user_cards.append(dealcard())
user_cards.append(dealcard())
comp_cards.append(dealcard())


def compare():
  if calculate_score(user_cards) == calculate_score(comp_cards):
    print("Its a draw")
  elif calculate_score(comp_cards) == 0:
    print("You loose!")
  elif calculate_score(user_cards) == 0:
    print("You win!")
  elif (calculate_score(user_cards) > 21) and calculate_score(comp_cards) < 21:
    print("You loose!")
  elif (calculate_score(comp_cards) > 21) and calculate_score(user_cards) < 21:
    print("You win!")
  elif calculate_score(comp_cards) > calculate_score(user_cards):
    print("You loose!")
  elif calculate_score(comp_cards) < calculate_score(user_cards):
    print("You win!")

play_blackjack = input("Would you like to play Blackjack? Type y or n: ")
while play_blackjack == "y":
  #clear()
  #print(logo)
  print(f"Your cards are {user_cards}, with a total {sum(user_cards)}")
  print(f"Computer cards are {comp_cards}, with a total {sum(comp_cards)}")
  keep_playing = input("Would you like another card? y or n?\n")
  while keep_playing == "y":
    user_cards.append(dealcard())
    print(f"Your cards are {user_cards}, with a total {sum(user_cards)}")
    keep_playing = input("Would you like another card? y or n?\n")

  comp_total = calculate_score(comp_cards)
  while comp_total < 17:
    comp_cards.append(dealcard())
    comp_total = calculate_score(comp_cards)
  print(f"Comp cards are {comp_cards}, with a total {sum(comp_cards)}")
  compare()
  play_blackjack = input("Would you like to play Blackjack? Type y or n: ")






