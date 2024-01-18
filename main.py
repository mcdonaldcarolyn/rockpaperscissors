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
        
        if playerMove == 'R' or playerMove == 'P' or playerMove =='S':
            break
        else:
            print('type one of R, P, S, or Q')

    if playerMove == 'R':
        print( 'ROCK versus...')
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('PAPER versus...')
        playerMove = 'PAPER'
    elif playerMove == 'S':
        print('SCISSORS versus...')
        playerMove = 'SCISSORS'

    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3....')
    time.sleep(0.25)

    if playerMove == computerMove:
        print('It\s a tie!')
        ties = ties + 1
     
