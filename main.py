'''
"Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"
source: https://en.wikipedia.org/wiki/Monty_Hall_problem
'''

# This code is a simulation to show what happens if to switch
from random import randint

player_won = player_defeats = 0
numbers_of_matches = 1000
for _ in range(numbers_of_matches):
    car_is = randint(1, 3)
    player_choice = randint(1, 3)
    opened_door = car_is
    
    while opened_door == player_choice or opened_door == car_is:
        opened_door = randint(1, 3)
        
    if (player_choice == 2 and opened_door == 3) or (player_choice == 3 and opened_door == 2):
        player_choice = 1
    elif (player_choice == 1 and opened_door == 3) or (player_choice == 3 and opened_door == 1):
        player_choice = 2
    elif (player_choice == 1 and opened_door == 2) or (player_choice == 2 and opened_door == 1):
        player_choice = 3
        
    if player_choice == car_is:
        player_won += 1
    else:
        player_defeats += 1
        
print(f'Player is with {(player_won/numbers_of_matches*100):.2f}% wins and {(player_defeats/numbers_of_matches*100):.2f}% defeats ')
    