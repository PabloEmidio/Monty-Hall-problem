'''
"Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"
source: https://en.wikipedia.org/wiki/Monty_Hall_problem
'''

# This code is a simulation to show what happens if to switch
from random import randint
import sys

player_won = 0

if len(sys.argv)>1 and sys.argv[1].isdigit():
    numbers_of_matches = int(sys.argv[1]) 
else:
    sys.exit('Monty Hall problem: parameters error')

for _ in range(numbers_of_matches):
    car_is = opened_door = randint(1, 3) # the opened door will be based on where the car is
    player_choice = randint(1, 3)
    
    while opened_door in (car_is, player_choice):
        opened_door = randint(1, 3)
        
    if (player_choice == 2 and opened_door == 3) or (player_choice == 3 and opened_door == 2):
        player_choice = 1
    elif (player_choice == 1 and opened_door == 3) or (player_choice == 3 and opened_door == 1):
        player_choice = 2
    elif (player_choice == 1 and opened_door == 2) or (player_choice == 2 and opened_door == 1):
        player_choice = 3
        
    if player_choice == car_is:
        player_won += 1


print(f'{numbers_of_matches} matches done, switching the door it\'d win {player_won} times, {(player_won/numbers_of_matches*100):.1f}% of the matches')
if numbers_of_matches<=200:
    print('\n\n\033[1;31mThe simulation is more accurate when number of matches is greater than 200\033[m')