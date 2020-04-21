import random

print('Welcome to HNG Guessing Game')
print('____________________________')
print('')

def easy_level():
    secret_num = random.randint(1,10)
    no_of_guess = 0
    guess_limit = 6

    while no_of_guess < guess_limit:
        try:
            guess = int(input('Guess the secret number from 1 to 10: '))
            no_of_guess += 1
            if guess == secret_num:
                print('You got it right!')
                break
            elif guess != secret_num:
                guess_left = guess_limit - no_of_guess
                print('That was wrong')
                print(f'You have {guess_left} guesses left')
        except ValueError:
            print('Only numbers allowed')
    else:
        print('Game Over!')


def middle_level():
    secret_num = random.randint(1,20)
    no_of_guess = 0
    guess_limit = 4

    while no_of_guess < guess_limit:
        try:
            guess = int(input('Guess the secret number from 1 to 20: '))
            no_of_guess += 1
            if guess == secret_num:
                print('You got it right!')
                break
            elif guess != secret_num:
                guess_left = guess_limit - no_of_guess
                print('That was wrong')
                print(f'You have {guess_left} guesses left')
        except ValueError:
            print('Only numbers allowed')
    else:
        print('Game Over!')


def hard_level():
    secret_num = random.randint(1,50)
    no_of_guess = 0
    guess_limit = 3

    while no_of_guess < guess_limit:
        try:
            guess = int(input('Guess the secret number from 1 to 50: '))
            no_of_guess += 1
            if guess == secret_num:
                print('You got it right!')
                break
            elif guess != secret_num:
                guess_left = guess_limit - no_of_guess
                print('That was wrong')
                print(f'You have {guess_left} guesses left')
        except ValueError:
            print('Only numbers allowed')
    else:
        print('Game Over!')

status = True

while status:
    diff_level = input('Enter difficulty level (easy, middle or hard): ')
    if diff_level.lower() == 'easy':
        easy_level()
        break
    elif diff_level.lower() == 'middle':
        middle_level()
        break
    elif diff_level.lower() == 'hard':
        hard_level()
        break


