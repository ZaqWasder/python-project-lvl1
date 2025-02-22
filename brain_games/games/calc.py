from random import choice, randint

MIN_NUMBER = 0
MAX_NUMBER = 100
OPERATORS = ["+", "-", "*"]
RULES = 'What is the result of the expression?'


def get_challenge():
    first_operand = randint(MIN_NUMBER, MAX_NUMBER)
    second_operand = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(OPERATORS)
    question = f'{first_operand} {operator} {second_operand}'
    answer = get_answer(first_operand, second_operand, operator)
    return (question, answer)


def get_answer(first_operand, second_operand, operator):
    match operator:
        case '+':
            answer = first_operand + second_operand
        case '-':
            answer = first_operand - second_operand
        case '*':
            answer = first_operand * second_operand

    return answer
