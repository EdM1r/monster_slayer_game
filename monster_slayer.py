
import random
import os

#starting parameters
player_life = 100
player_damage = 10 
player_money  = 10
player_kill_count = 0 
player_data_array = [player_life, player_damage, player_money, player_kill_count]

#battle function 
def battle(player_data_array):
  monster_life = random.randint(5,50)
  monster_damage = random.randint(1,10)
  print('You face a Monster with', monster_life, 'health points!')
  battling = True
  while battling == True:
    print('Your life is ', player_data_array[0])
    print('Your attack deals' , player_data_array[1], 'damage to monster.')
    monster_life -= player_data_array[1]
    print('Monster attack deals' , monster_damage, 'damage!')
    player_data_array[0] -= monster_damage
    if player_data_array[0] <= 0:
      print("You died...")
      print('In your career you defeated:', player_data_array[3], 'monsters!')
      quit()
    elif monster_life <= 0:
      print("You slayed the monster!")
      player_data_array[2] += 10
      player_data_array[3] += 1
      break
    else:
      input('Hit [enter] to continue fight!')
  return player_data_array

#playing code 
exit = False
while exit == False:
  print('-' * 20)
  print('Health:', player_data_array[0])
  print('Coins:', player_data_array[2])
  print("[1] Fight the monster")
  print("[2] Buy upgrade weapon (costs 10 coins)")
  print("[3] Buy heal potion (costs 10 coins and heals 50 Helth)")
  print('[9] Exit')
  player_choise = input('Choose next action:')
  if player_choise == '1':
    player_data_array = battle(player_data_array)
  elif player_choise == '2':
    if player_data_array[2] >= 10:
      player_data_array[1] += 1
      player_data_array[2] -= 10
      print('You upgraded your weapon, now it deals', player_data_array[1], 'damage.')
    else:
      print('Not enough coins! Try to earn coins slaying monsters.')
  elif player_choise == '3':
    if player_data_array[2] >= 10:
      player_data_array[0] = player_data_array[0] + 50 if player_data_array[0] <=50 else 100
      player_data_array[2] -= 10
    else:
      print('Not enough coins! Try to earn coins slaying monsters.')
  elif player_choise == '9':
    exit = True
    print('You exit the game. In your career you defeated:', player_data_array[3], 'monsters!')
  else:
    print('This is not legit option, try another one.')




    