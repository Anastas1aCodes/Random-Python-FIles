# Enhanced - Outputs numbers that have been guessed & the number of guesses that it took to guess the correct number

from random import randint as rI
num,guessList=rI(1,100),[]
while 1:
    print(num)
    guess=int(input('Guess a number: '))
    guessList.append(guess)
    if guess<num:print(f'Your number is lower!\nYou guessed: {guessList}')
    elif guess>num:print(f'Your number is higher!\nYou guessed: {guessList}')
    elif guess==num and input(f'You took {len(guessList)} guesses to guess the correct answer!\nWould you like to play again? (Y/N)').lower() == 'n':break
    else:num,guessList=rI(1,100),[]
