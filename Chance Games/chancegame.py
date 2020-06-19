#Was able to incorporate the coin flip, cho han, and card war games. Don't know how roulettes work. Might revisit
#this project later down the line after I learn how roulettes. Might not. Who knows :)

import random #imports the random module

money = 100 #starting value of money

num = random.randint(1, 10) #generates a random between 1 and 10 inclusive

#flips coin
def coin_flip(guess, bet):
    if(bet <= 0):   #checks for valid bet
        return "Cmon, you gotta bet more than 0 -_-"
    global money    #allows access to variable money
    flip = random.randint(1, 2)
    if(flip == 1):
        toss = "Heads"
    else:
        toss = "Tails"
    #introduction to the game
    print("Welcome to the coin flip game! If your guess was correct, then the amount you bet will be added to your money total. " +
    "The flip this round resulted in a " + toss + ". You guessed: " + guess + ". The amount you bet was: " + str(bet) + ".")
    if(guess == toss):
        money = money + bet     #adds bet to balance
        return "You won!! Your bet will be added to your total money. Your current balance is " + str(money)
    else:
        money = money - bet     #subtracts bet from balance
        return "You lost :( Your bet will be deducted from your total money. Your current balance is " + str(money)

def cho_han(guess, bet):
    if(bet <= 0):
        return "Cmon, you gotta bet more than 0 -_-"
    global money
    dice1 = random.randint(1,6)     #result of dice 1
    dice2 = random.randint(1,6)     #result of dice 2
    sum = dice1 + dice2
    if((sum % 2) > 0):              #odd sums
        roll = "Odd"
    else:
        roll = "Even"
    print("")
    #introduction to the game
    print("Welcome to the Cho Han game! If your guess was correct, then the amount you bet will be added to your money total. " +
    "The roll this round resulted in a sum that was " + roll + ". You guessed: " + guess + ". The amount you bet was: " + str(bet) + ".")
    if(guess == roll):
        money = money + bet     #adds bet to balance
        return "You won!! Your bet will be added to your total money. Your current balance is " + str(money)
    else:
        money = money - bet     #subtracts bet from balance
        return "You lost :( Your bet will be deducted from your total money. Your current balance is " + str(money)

def card_war(bet):
    if(bet <= 0):
        return "Cmon, you gotta bet more than 0 -_-"
    global money
    player1_card = random.randint(1, 14)
    player2_card = random.randint(1, 14)
    print("")
    print("Welcome to the Card War game! You are player 1. If your card is higher than player 2, you win. Jacks, Queens, Kings, and Aces"
    + " are represented by 11, 12, 13, and 14 correspondingly. You drew a " + str(player1_card) + ". Player 2 drew a " + str(player2_card) +
    ". The amount you bet was: " + str(bet) + ".")
    if(player1_card > player2_card):
        money = money + bet     #adds bet to balance
        return "You won!! Your bet will be added to your total money. Your current balance is " + str(money)
    else:
        money = money - bet     #subtracts bet from balance
        return "You lost :( Your bet will be deducted from your total money. Your current balance is " + str(money)


# def roulette(number_guess, boolean_guess, bet):     #don't really know how roulettes work..so this function isn't entirely accurate to the game
#     global money
#     space = random.randint(1, 100)
#     if((space % 2) > 0):
#         guess = "Odd"
#     else:
#         guess = "Even"
#     print("")
#     print("Welcome to roulettes! You have the option to guess a number between 1 to 100. If your guess matches with the space, then you win " +
#     "your bet multiplied by 35. If not, then your bet is deducted from your total. You also have the option to guess if the space is " +
#     "odd or even. Your guess for the numbered space is: " + str(number_guess) + ". Your guess for if it is odd or even is: " + str(boolean_guess) +
#     ". The real number is: " + str(space) + ". The space is also: " + guess + ". The amount you bet was: " + str(bet) + ".")
#     if(number_guess == space):
#         money = money + (bet * 35)
#         return "You won!! Your bet will be added to your total money. Your current balance is " + str(money)
#     elif(boolean_guess == guess):
#         money = money + bet
#         return "You won!! Your bet will be added to your total money. Your current balance is " + str(money)
#     elif(boolean_guess != guess):
#         money = money - bet
#         return "You lost :( Your bet will be deducted from your total money. Your current balance is " + str(money)
#     else:
#         money = money - (bet * 35)
#         return "You lost :( Your bet will be deducted from your total money. Your current balance is " + str(money)
    #yeah..this roulette game is not accurate at all and im not sure how roulettes work lol

print(coin_flip("Heads", 100))
print(cho_han("Odd", 100))
print(card_war(100))
#print(roulette("Even", 76, 100))
print("")
print("The total amount of money you have is: " + str(money))
