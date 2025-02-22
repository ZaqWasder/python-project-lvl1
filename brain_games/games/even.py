from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

def get_challenge():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    answer = get_answer(question)
    return (question, answer)


def get_answer(question):
    return 'yes' if question % 2 == 0 else 'no'
