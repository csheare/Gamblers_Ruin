'''
Filename: main.py

Used to ...
'''

from players import Player,Players
from gamble import Gamble

if __name__ == '__main__':
    '''
    Main method to call 
    '''
    print("Enter Player 1 odds of winning")
    p1_p = float(input())
    print("Enter Player 1 inital wealth")
    p1_w = int(input())

    print("Enter Player 2 odds of winning")
    p2_p = float(input())
    print("Enter Player 2 inital wealth")
    p2_w = int(input())

    player1 = Player(p1_p,p1_w)
    player2 = Player(p2_p,p2_w)
    players = Players([player1,player2])

    answer = 'y'
    game_num = 1;
    while(answer == 'y'):
        print("How many Games?")
        games = int(input())

        print("Gamble Number: " + str(game_num))
        gamble = Gamble(players)
        game_num = gamble.play(games, game_num)
        print("Would you like to Gamble Again?(y/n)")
        answer = input()


    print("Thanks for Playing!!")
