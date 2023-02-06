from random import randint as rI
num=rI(1,100)
while 1:
    guess=int(input('Guess a number: '))
    if guess<num:print('Your number is lower!')
    elif guess>num:print('Your number is higher!')
    elif guess==num and input('You have guessed the correct number!\nWould you like to play again? (Y/N)').lower() == 'n':break
    else:num=rI(1,100)
