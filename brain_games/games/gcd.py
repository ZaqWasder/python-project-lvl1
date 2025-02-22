from random import randint

MIN_NUMBER = 0
MAX_NUMBER = 100
RULES = 'Find the greatest common divisor of given numbers.'


def get_challenge():
    first_num = randint(MIN_NUMBER, MAX_NUMBER)
    second_num = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{first_num} {second_num}'
    answer = get_gcd(first_num, second_num)

    return (question, answer)


def get_gcd(first_num, second_num):
    if first_num == second_num:
        return first_num

    min_num = min(first_num, second_num)
    max_num = max(first_num, second_num)

    return get_gcd(min_num, max_num - min_num)
