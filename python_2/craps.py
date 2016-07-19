#!python
"""craps.

Create a program that calls a function that simulates the rolling of a pair
of dice.
*   Your main program will deal with the total of the two dice.
*   The rules are as follows:
  *   On the first roll, a total of 7 or an 11 is an automatic win
  *   On the first roll, a total of 2, 3 or 12 is an automatic loss
  *   Any other number is called the Point.
  *   Keep rolling the dice until one of the following occurs:
      *   You roll a 7 which is a loss
      *   You roll the Point number again which is a win.
*   You start with $100 and bet $10 on each play.
*   Print all the rolls and whether you have won or lost on one line.
*   Print the funds balance and a request to play again on the next line.
    *   A 'y' or 'Y' means play again. Anything else ends play.
    *   A balance of $0 ends play automatically.
"""

from random import randrange

balance = 100
bet_amt = 10
this_roll = 0


def roll_dice(num_dice):
    """roll num_dice die."""
    sum_rolls = 0
    i = 0
    while i < num_dice:
        sum_rolls += randrange(1, 7)
        i += 1
    return sum_rolls


def win(bet_amt):
    global balance
    print "You win!",
    balance += bet_amt


def lose(bet_amt):
    global balance
    print "You lose!",
    balance -= bet_amt

# welcome
print "Beginning Balance = $%i" % balance

# first roll
this_roll = roll_dice(2)
print this_roll,

if this_roll == 7 or this_roll == 11:
    win(bet_amt)
elif this_roll == 2 or this_roll == 3 or this_roll == 12:
    lose(bet_amt)
else:
    # roll again
    point = this_roll
    while True:
        this_roll = roll_dice(2)
        print this_roll,
        if this_roll == 7:
            lose(bet_amt)
            break
        elif this_roll == point:
            win(bet_amt)
            break
        else:
            continue


# play again?

# choice = raw_input("Play again? y/n: ").lower

# if choice == 'y':
#     continue
# else:
#     break
