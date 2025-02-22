
from random import randint

RULES = 'What number is missing in the progression?'
PROGRESSION_MIN_START_ELEMENT = 0
PROGRESSION_MAX_START_ELEMENT = 10
PROGRESSION_MIN_LENGTH = 5
PROGRESSION_MAX_LENGTH = 10
PROGRESSION_MIN_STEP = 2
PROGRESSION_MAX_STEP = 10


def get_challenge():
    progression_start = randint(
        PROGRESSION_MIN_START_ELEMENT,
        PROGRESSION_MAX_START_ELEMENT
    )
    progression_length = randint(
        PROGRESSION_MIN_LENGTH,
        PROGRESSION_MAX_LENGTH
    )
    progression_step = randint(
        PROGRESSION_MIN_STEP,
        PROGRESSION_MAX_STEP
    )
    hidden_elem_index = randint(0, progression_length - 1)
    progression = [i * progression_step
                   for i in range(progression_start,
                                  progression_start + progression_length)]
    hidden_elem = progression[hidden_elem_index]
    progression[hidden_elem_index] = '..'
    question = ' '.join(map(str, progression))
    answer = hidden_elem

    return (question, answer)
