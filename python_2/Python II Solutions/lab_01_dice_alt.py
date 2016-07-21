"""lab_01_dice_alt.py

This module is a modification of the original dice game.  It simply
continues play until there is no more money.  Also, it uses the randint
function instead of randrange and it uses the older method of formatting
"""

def dice_rolls():
    from random import randint 
    temp1 = randint(1,6)
    temp2 = randint(1,6)
    return temp1 + temp2 

money = 100
plays = 0
max_play = 0
max_money = money
win_lose = ''
print 'Beginning Balance = $%d' % money
while True:
    plays = plays + 1
    firstroll = True
    while True:
        myroll = dice_rolls()
        print myroll,
        if firstroll:
            if myroll < 4 or myroll == 12:
                win_lose = 'L'
                break
            if myroll == 7 or myroll == 11:
                win_lose = 'W'
                break
            point = myroll
            firstroll = False
            continue
        if myroll == 7:
            win_lose = 'L'
            break
        if myroll == point:
            win_lose = 'W'
            break
    if win_lose == 'L':
        money = money - 10
        print 'You lose!'
        if money <= 0:
            break
    if win_lose == 'W':
        money = money + 10
        print 'You win!'
        if money > max_money:
            max_money = money
            max_play = plays
    print 'Balance = $%d -' % money,
#    contin = raw_input('Play again? y/n: ')
#    if contin != 'y' and contin != 'Y':
#        break
print '\nNumber of plays -', plays
print 'Ending Balance = $%d' % money
print 'Maximum money at play %d = %d' % (max_play, max_money)
        
    
        
            
