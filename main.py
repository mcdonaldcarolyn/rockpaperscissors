import random, time, sys

print('''rock paper scissors bu invent eith python''')

wins = 0 
losses = 0 
ties = 0

while True:
    while True:
        print('{} Wins, {} losses, {} ties'.format(wins, losses, ties))
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()