import random


print("Welcome to the Dice Game! 🎲")
bet_dollars = int(input("How much would you like to bet?: "))
roll_dice = input('Type in "roll" to roll the dice: ')
roll_dice = roll_dice.lower()
if roll_dice == "roll":
  dice_roll = random.randint(1, 6)
  dice_roll2 = random.randint(1, 6)
  print(f"You rolled {dice_roll} & {dice_roll2} 🎲 🎲")
user_total = (dice_roll + dice_roll2)
print("It is your opponents turn...")
opp_roll_dice = random.randint(1, 6)
opp_roll_dice2 = random.randint(1, 6)
opp_total = (opp_roll_dice + opp_roll_dice2)
print(f"Your opponent rolled {opp_roll_dice} & {opp_roll_dice2} 🎲 🎲 ")
if user_total > opp_total:
  print(f"You win! ${bet_dollars}!")
  if dice_roll == dice_roll2:
    print(f"You rolled a double and got a bonus{bet_dollars}")
if user_total == opp_total:
  print("It's a draw! You get your bet back!")
if user_total < opp_total:
  print(f"You lose! You lost ${bet_dollars}!")

dollar_start = 100
if user_total > opp_total:
  dollar_win = (dollar_start + bet_dollars)
  print(f"You now have ${dollar_win} !")
  win = True
if user_total < opp_total:
  dollar_loss = (dollar_start - bet_dollars)
  print(f"You now have ${dollar_loss} !")
  lose = True
  if dollar_loss < 0:
    print("You now have a negative balance and are in debt.")












