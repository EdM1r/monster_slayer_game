
import random
import os

#starting parameters
player_life = 100
player_damage = 10 
player_money  = 10
player_kill_count = 0 


#battle function 
def battle(player_life, player_damage, player_money, player_kill_count):
  monster_life = random.randint(5,50)
  monster_damage = random.randint(1,10)
  print('You face a Monster with', monster_life, 'health points!')
  battling = True
  while battling == True:
    print('Your life is ', player_life)
    print('Your attack deals' , player_damage, 'damage to monster.')
    monster_life -= player_damage
    print('Monster attack deals' , monster_damage, 'damage!')
    player_life -= monster_damage
    if player_life <= 0:
      print("You died...")
      print('In your career you defeated:', player_kill_count, 'monsters!')
      quit()
    elif monster_life <= 0:
      print("You slayed the monster!")
      player_money += 10
      player_kill_count += 1
      break
    else:
      input('Hit [enter] to continue fight!')
  return player_life, player_damage, player_money, player_kill_count

#playing code 
exit = False
while exit == False:
  print('-' * 20)
  print('Health:', player_life)
  print('Coins:', player_money)
  print("[1] Fight the monster")
  print("[2] Buy upgrade weapon (costs 10 coins)")
  print("[3] Buy heal potion (costs 10 coins and heals 50 Helth)")
  print('[9] Exit')
  player_choise = input('Choose next action:')
  if player_choise == '1':
    player_life, player_damage, player_money, player_kill_count = battle(player_life, player_damage, player_money, player_kill_count)
  elif player_choise == '2':
    if player_money >= 10:
      player_damage += 1
      player_money -= 10
      print('You upgraded your weapon, now it deals', player_damage, 'damage.')
    else:
      print('Not enough coins! Try to earn coins slaying monsters.')
  elif player_choise == '3':
    if player_money >= 10:
      player_life = player_life + 50 if player_life <=50 else 100
      player_money -= 10
    else:
      print('Not enough coins! Try to earn coins slaying monsters.')
  elif player_choise == '9':
    exit = True
    print('You exit the game. In your career you defeated:', player_kill_count, 'monsters!')
  else:
    print('This is not legit option, try another one.')




    