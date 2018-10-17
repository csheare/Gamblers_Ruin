
from players import Players,Player
import random
import sys

class Gamble:

    def __init__(self, players):
        self.players = players


    def play(self,num_games,total_games):

        current_games = total_games
        for i in range(num_games):
            print("Game Number: "+ str(current_games))
            rand = random.uniform(0,1)
            print("Rand is: " +str(rand))
            if rand <= self.players.player1.prob:
                self.players.player1.update(True)
                self.players.player2.update(False)
            else:
                self.players.player1.update(False)
                self.players.player2.update(True)
            print("Player 1 has %d wins and %d money" %(self.players.player1.total_wins, self.players.player1.money))
            print("Player 2 has %d wins and %d money" %(self.players.player2.total_wins, self.players.player2.money))
            if(self.players.player1.money == 0 or self.players.player2.money ==0):
                print("Game Over!")
                if(self.players.player1.money):
                    print("Player 1 Wins!")
                else:
                    print("Player 2 Wins!")
                sys.exit()

            current_games +=1
