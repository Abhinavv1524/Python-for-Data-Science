import random 
choices = ['Rock', 'Paper', 'Scissors']

player_point = 0
computer_point = 0

while True:
    computer_choice = random.choice(choices)
    print("")
    player_choice = input("Rock, Paper or Scissor? ").capitalize()

    if(computer_choice == player_choice):

        print('its a tie')
    
    elif(player_choice == 'Rock'):
        if(computer_choice == 'Paper'):
            print('Player won')
            print('you have choosed ' + player_choice + ' and computer has choosed '+computer_choice)
            player_point = player_point + 1
        else:
            print('Player won')
            print('you have choosed ' + player_choice + ' and computer has choosed '+computer_choice)
            player_point = player_point + 1

    elif (player_choice == 'Paper'):
        if(computer_choice == 'Rock'):
            print('Computer won')
            print('you have choosed ' + player_choice + ' and computer has choosed '+computer_choice)
            computer_point = computer_point + 1
        else:
            print('Computer won')
            print('you have choosed ' + player_choice + ' and computer has choosed '+computer_choice)
            computer_point = computer_point + 1

    elif (player_choice == 'Scissor'):
        if(computer_choice == 'Rock'):
            print('Computer won')
            print('you have choosed ' + player_choice + ' and computer has choosed '+computer_choice)
            computer_point = computer_point + 1
        else:
            print('Player won')
            print('you have choosed ' + player_choice + ' and computer has choosed '+computer_choice)
            player_point = player_point + 1
    
    else :
        break

if(player_point > computer_point):
    print('Player won with ',player_point, ' points')
elif(player_point == computer_point):
    print('its a tie')
else:
    print('Computer won with ',computer_point ,' points')