class Players:

    def __init__(self,players):
        self.players = players
        self.player1 = players[0]
        self.player2 = players[1]

        total_p = sum(player.prob for player in players)

        if(total_p != 1):
            raise ValueError("PMF is invalid\nProbabilities do not sum to one")

        print("Players Inititalized with total_p:" + str(total_p))

class Player:

    def __init__(self,p,m):
        self.prob = p
        self.initial_money = m
        self.money = m
        self.total_wins = 0
        self.total_loses = 0


    
    def update(self,win):
        if(win):
            self.money += 1
            self.total_wins +=1
        else:
            self.money -= 1
            self.total_loses +=1
