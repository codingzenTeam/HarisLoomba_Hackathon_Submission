import random

class snakesAndLadders:
    def __init__(self, playerA, playerB):
        self.LADDERS = {
            4:56,
            12:50,
            14:55,
            22:58,
            41:79,
            54:88   
        }
        self.SNAKES = {
            28:10,
            37:3,
            47:16,
            75:32,
            94:71,
            96:42
        }

        self.playerA = playerA
        self.playerB = playerB

        self.playerAScore = 0
        self.playerBScore = 0
        self.HIT = 100

        self.win = None

    def winning(self, win: bool):
        if bool(win):
            print('Player B has won!')
            quit()
        elif not bool(win):
            print('Player A has won!')
            quit()
        else:
            print('Error Occured!')
            quit()

    def checkScore(self):
        if self.playerAScore==self.HIT:
            self.win = 0
        elif self.playerBScore==self.HIT:
            self.win = 1
        else:
            return None
        self.winning(self.win)

    def chance(self, player):
        move = random.randint(1, 6)
        print(f'Dice roll: {move} \n')
        if bool(player):
            if self.playerBScore+move>self.HIT:
                print('Player B moves 0 steps due to not a perfect 100, ', f'{self.HIT-self.playerBScore} Steps to go')
                return None
            if self.playerBScore+move in list(self.LADDERS.keys()):
                print('Player B Has Caught a ladder! Reaching, ' + str(self.LADDERS[self.playerBScore+move]))
                self.playerBScore=self.LADDERS[self.playerBScore+move]
            elif self.playerBScore+move in list(self.SNAKES.keys()):
                print('Player B has caught a Snake! backing to, ' + str(self.SNAKES[self.playerBScore+move]))
                self.playerBScore=self.SNAKES[self.playerBScore+move]
            else:
                print(f'Player B Moved {move} Steps!', 'Reaching, ' + str(move+self.playerBScore))
                self.playerBScore+=move
            print('Player B Score ' + str(self.playerBScore))

        elif not bool(player):
            if self.playerAScore+move>self.HIT:
                print('Player A moves 0 steps due to not a perfect 100, ', f'{self.HIT-self.playerAScore} Steps to go')
                return None
            if self.playerAScore+move in list(self.LADDERS.keys()):
                print('Player A Has Caught a ladder! Reaching, ' + str(self.LADDERS[self.playerAScore+move]))
                self.playerAScore=self.LADDERS[self.playerAScore+move]
            elif self.playerAScore+move in list(self.SNAKES.keys()):
                print('Player A has caught a Snake! backing to, ' + str(self.SNAKES[self.playerAScore+move]))
                self.playerAScore=self.SNAKES[self.playerAScore+move]
            else:
                print(f'Player A Moved {move} Steps!', 'Reaching, ' + str(move+self.playerAScore))
                self.playerAScore+=move

            print('Player A Score ' + str(self.playerAScore))
        else:
            print('Error Occured!')
            quit()

        self.checkScore()

print('Welcome to SnakesNLadders. A Classic Game!')
playerA = input('Player 1 Name - ')
playerB = input('Player 2 Name - ')
game = snakesAndLadders(playerA, playerB)
while True:
    input('Player A Chance, Press Enter to roll the dice!')
    game.chance(0)
    input('Player B Chance, Press Enter to roll the dice!')
    game.chance(1)
