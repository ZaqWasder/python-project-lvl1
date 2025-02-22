from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_challenge():
    num = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{num}'
    answer = 'yes' if is_prime(num) else 'no'

    return (question, answer)


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True
