from random import choice


class SameNumbersError(Exception):
    pass


class WrongNumberLengthError(Exception):
    pass


def take_data():
    while True:

        try:
            length = int(input('Please type the length of the number (max 10): '))

            if not 1 <= length <= 10:
                raise WrongNumberLengthError

        except ValueError:
            print('Error, player input must be a number.')

        except WrongNumberLengthError:
            print('Error, player input must be a number with length of 1 to 10 numbers.')

        else:
            break

    return length


def random_number_generator(length: int):
    generated_number = []
    n_range = [n for n in range(1, 10)]

    for i in range(length):
        random_number = choice(n_range)
        n_range.remove(random_number)

        generated_number.append(random_number)

        if i == 0:
            n_range.append(0)

    return generated_number


def matching_numbers(generated_number, current_player_numbers, n_length, current_turn):
    bulls = [generated_number[i] for i in range(len(generated_number)) if generated_number[i] == player_numbers[i]]
    cows = [n for n in generated_number if n in current_player_numbers and n not in bulls]

    bulls_amount = len(bulls)
    cows_amount = len(cows)

    if bulls_amount != n_length:
        return f'{current_turn}: {bulls_amount} bulls and {cows_amount} cows.', False

    else:
        return f'{current_turn}: {bulls_amount} bulls! You won!\nAnswer: {"".join(map(str, generated_number))}', True


n_tries = 10
number_length = take_data()
comp_num = random_number_generator(number_length)
turn = 0
won = False

print('''You have 10 tries. Guess the number!
Note: The number doesn't start with 0.''')
while n_tries != turn and not won:

    try:
        player_numbers = list(map(int, input(f'Please type а {number_length}-digit number.\n')))

        if len(player_numbers) != number_length:
            raise WrongNumberLengthError

        if len(set(player_numbers)) != number_length:
            raise SameNumbersError

        turn += 1

        message, won = matching_numbers(comp_num, player_numbers, number_length, turn)

        print(message)

    except ValueError:
        print('Error, player input must be a number. Please try again.')

    except SameNumbersError:
        print('Player number must have different digits.')

    except WrongNumberLengthError:
        print(f'Player number must be of {number_length}-digit length.')

if not won:
    print(f'You lost. Better luck next time.\nAnswer: {"".join(map(str, comp_num))}')