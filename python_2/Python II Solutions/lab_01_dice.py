"""lab_01_dice.py

This program simulates a craps game.  It is designed to demonstrate
the use of loops and decision making structures.  Note the use of the
randrange function instead of the less Pythonic randint.  It is
important to know the difference between the two.
"""

from random import randrange 
def dice_rolls():
    return randrange(1,7) + randrange(1,7) 

money = 100
plays = 0
print 'Beginning Balance = ${0:,d}'.format(money)
# print 'Beginning Balance = $%d' % money  # Older formatting
while True: # Loop that controls the continuation of the game
    plays = plays + 1
    firstroll = True
    win_lose = ''
    while win_lose == '':  # Loop that controls the individual wins/losses
        myroll = dice_rolls()
        print myroll,
        if firstroll:
            if myroll < 4 or myroll == 12:
                win_lose = 'L'
                continue
            if myroll == 7 or myroll == 11:
                win_lose = 'W'
                continue
            point = myroll
            firstroll = False
            continue
        if myroll == 7:
            win_lose = 'L'
            continue
        if myroll == point:
            win_lose = 'W'
            continue
    if win_lose == 'L':
        money = money - 10
        print 'You lose!'
        if money <= 0:
            break
    if win_lose == 'W':
        money = money + 10
        print 'You win!'
    print 'Balance = ${0:,d}'.format(money),
    contin = raw_input('Play again? y/n: ')
    if contin != 'y' and contin != 'Y':
        break
print '\nNumber of plays -', plays
print 'Ending Balance = ${0:,d}'.format(money)
# print 'Ending Balance = $%d' % money  # Older formatting
        
    
        
            
